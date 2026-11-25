"""Compara dois modelos de linguagem no assistente de RAG do capítulo de LLM.

A avaliação roda fora do livro, porque faz dezenas de chamadas à API e os
resultados mudariam a cada renderização. O script grava uma linha por
pergunta e modelo em data/avaliacao_modelos.csv, que o capítulo lê no anexo.

Uso, na pasta do projeto, com a chave OPENAI_API_KEY definida (no ambiente
ou no arquivo .Renviron):

    python scripts/avaliacao_rag.py              # avaliação completa
    python scripts/avaliacao_rag.py --piloto 2   # só as 2 primeiras perguntas
"""

import argparse
import os
import re
import time

import pandas as pd

# ---- mesmos parâmetros do capítulo ----
CAMINHO_PDF = "data/ggplot2.pdf"
CAMINHO_PERGUNTAS = "data/perguntas_teste.csv"
PUBLICO = "pessoas que estão aprendendo a fazer gráficos no R"
DOCUMENTO = "a documentação do pacote ggplot2"
IDIOMA_DOCUMENTO = "inglês"
TAMANHO_PEDACO = 1000
SOBREPOSICAO = 200
K = 4
MODELO_EMBEDDING = "text-embedding-3-small"

# ---- modelos comparados ----
# Modelos com raciocínio interno (como a família gpt-5) não aceitam
# temperature = 0, por isso cada modelo tem os próprios parâmetros.
MODELOS = {
    "gpt-4o-mini": {"model": "openai:gpt-4o-mini", "temperature": 0},
    "gpt-5.5": {"model": "openai:gpt-5.5"},
}

PADRAO_ABSTENCAO = re.compile(
    r"não (encontrei|foi encontrad|está (no|nos|presente)|consta|há informaç|tenho informaç"
    r"|posso responder|consigo responder)|fora do escopo",
    flags=re.IGNORECASE,
)


def carregar_chave():
    """Usa a chave do ambiente ou, se não houver, a do .Renviron (sem exibi-la)."""
    if os.environ.get("OPENAI_API_KEY") or not os.path.exists(".Renviron"):
        return
    for linha in open(".Renviron", encoding="utf-8"):
        m = re.match(r"\s*([A-Z_][A-Z0-9_]*)\s*=\s*(.*)\s*$", linha)
        if m:
            os.environ.setdefault(m.group(1), m.group(2).strip().strip('"').strip("'"))


def criar_banco_vetorial():
    from langchain_community.document_loaders import PyPDFLoader
    from langchain_core.vectorstores import InMemoryVectorStore
    from langchain_openai import OpenAIEmbeddings
    from langchain_text_splitters import RecursiveCharacterTextSplitter

    paginas = PyPDFLoader(CAMINHO_PDF).load()
    for p in paginas:   # mesma limpeza do capítulo
        p.page_content = (p.page_content
                          .replace("/quotesingle.Var", "'")
                          .replace("/grave.Var", "`"))
    divisor = RecursiveCharacterTextSplitter(
        chunk_size=TAMANHO_PEDACO, chunk_overlap=SOBREPOSICAO, add_start_index=True)
    vector_store = InMemoryVectorStore(OpenAIEmbeddings(model=MODELO_EMBEDDING))
    vector_store.add_documents(documents=divisor.split_documents(paginas))
    return vector_store


def criar_agente(vector_store, parametros):
    from langchain.agents import create_agent
    from langchain.chat_models import init_chat_model
    from langchain.tools import tool
    from langgraph.checkpoint.memory import InMemorySaver

    @tool(response_format="content_and_artifact")
    def buscar_no_documento(consulta: str):
        """Busca no documento os trechos relevantes para a consulta."""
        trechos = vector_store.similarity_search(consulta, k=K)
        texto = "\n\n".join(
            f"[página {d.metadata.get('page', 0) + 1}]\n{d.page_content}" for d in trechos)
        return texto, trechos

    prompt = (
        f"Você ajuda {PUBLICO} a consultar {DOCUMENTO}. "
        "Use a ferramenta buscar_no_documento para encontrar os trechos relevantes antes de responder. "
        "Responda em português do Brasil, de forma objetiva, somente com base nos trechos recuperados, "
        "e cite a página (por exemplo: p. 12). "
        "Se a informação não estiver nos trechos, diga que não encontrou no documento. "
        "Não responda perguntas fora do escopo do documento. "
        f"O documento está em {IDIOMA_DOCUMENTO}: formule a busca nesse idioma, mas responda em português."
    )
    return create_agent(init_chat_model(**parametros), tools=[buscar_no_documento],
                        system_prompt=prompt, checkpointer=InMemorySaver())


def paginas_citadas(texto):
    achados = re.findall(r"p(?:á|a)g(?:ina)?s?\.?\s*(\d+)|p\.\s*(\d+)", texto)
    return sorted({int(n) for par in achados for n in par if n})


def avaliar_pergunta(agente, linha, id_sessao):
    inicio = time.perf_counter()
    for tentativa in range(3):
        try:
            r = agente.invoke({"messages": [{"role": "user", "content": linha["pergunta"]}]},
                              config={"configurable": {"thread_id": id_sessao}})
            break
        except Exception as erro:   # limite de requisições ou falha temporária
            if tentativa == 2:
                raise
            print("  nova tentativa após erro:", type(erro).__name__)
            time.sleep(10 * (tentativa + 1))
    segundos = time.perf_counter() - inicio

    mensagens = r["messages"]
    ultimas = mensagens[max(i for i, m in enumerate(mensagens) if m.type == "human"):]
    consultas, consultadas, tok_in, tok_out = [], set(), 0, 0
    for m in ultimas:
        if m.type == "ai":
            consultas += [c["args"].get("consulta", "") for c in (m.tool_calls or [])]
            uso = getattr(m, "usage_metadata", None) or {}
            tok_in += uso.get("input_tokens", 0)
            tok_out += uso.get("output_tokens", 0)
        if m.type == "tool" and m.artifact:
            consultadas.update(d.metadata.get("page", 0) + 1 for d in m.artifact)

    resposta = mensagens[-1].text
    citadas = paginas_citadas(resposta)
    no_escopo = linha["tipo"] == "no_escopo"
    acertou = (any(int(linha["pagina_inicial"]) <= p <= int(linha["pagina_final"]) for p in consultadas)
               if no_escopo else None)
    return {
        "pergunta": linha["pergunta"],
        "tipo": linha["tipo"],
        "topico": linha["topico"],
        "consultas": " | ".join(consultas),
        "paginas_consultadas": " ".join(map(str, sorted(consultadas))),
        "paginas_citadas": " ".join(map(str, citadas)),
        "acertou_recuperacao": acertou,
        # citação fiel: todas as páginas citadas foram consultadas (vazio se não citou nenhuma)
        "citacao_fiel": (set(citadas) <= consultadas) if citadas else None,
        "absteve": bool(PADRAO_ABSTENCAO.search(resposta)),
        "tokens_entrada": tok_in,
        "tokens_saida": tok_out,
        "segundos": round(segundos, 1),
        "resposta": resposta,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--piloto", type=int, default=0,
                        help="avalia só as N primeiras perguntas (não grava o arquivo final)")
    parser.add_argument("--saida", default="data/avaliacao_modelos.csv")
    args = parser.parse_args()

    carregar_chave()
    perguntas = pd.read_csv(CAMINHO_PERGUNTAS, dtype=str, keep_default_na=False)
    if args.piloto:
        perguntas = perguntas.head(args.piloto)

    print("Criando o banco vetorial...")
    vector_store = criar_banco_vetorial()

    linhas = []
    for nome, parametros in MODELOS.items():
        agente = criar_agente(vector_store, parametros)
        for i, linha in perguntas.iterrows():
            print(f"{nome} | {i + 1}/{len(perguntas)} | {linha['pergunta'][:60]}")
            resultado = avaliar_pergunta(agente, linha, id_sessao=f"{nome}-{i}")
            linhas.append({"modelo": nome, **resultado})

    tabela = pd.DataFrame(linhas)
    resumo = tabela.groupby("modelo")[["tokens_entrada", "tokens_saida", "segundos"]].sum()
    print(resumo)

    if args.piloto:
        print("Piloto: arquivo não gravado.")
    else:
        tabela.to_csv(args.saida, index=False, encoding="utf-8")
        print("Resultados gravados em", args.saida)


if __name__ == "__main__":
    main()
