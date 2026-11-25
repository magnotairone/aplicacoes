# Executado pelo Quarto ao final de cada render (post-render em _quarto.yml),
# inclusive quando só um capítulo é renderizado. Escreve a data do dia no
# trecho "Última atualização" da página inicial do livro.
#
# A data não é calculada com código R no index.qmd porque o projeto usa
# freeze: o resultado ficaria congelado em _freeze/ até o index.qmd mudar.

import datetime
import os
import re

saida = os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_book")
hoje = datetime.date.today().strftime("%d/%m/%Y")

# index.html: o index.qmd marca a data com [..]{#data-atualizacao}
caminho = os.path.join(saida, "index.html")
if os.path.exists(caminho):
    with open(caminho, encoding="utf-8") as f:
        html = f.read()
    novo = re.sub(r'(<span id="data-atualizacao">)[^<]*(</span>)', rf"\g<1>{hoje}\g<2>", html)
    if novo != html:
        with open(caminho, "w", encoding="utf-8", newline="") as f:
            f.write(novo)

# search.json: mantém a busca do site coerente com a página
caminho = os.path.join(saida, "search.json")
if os.path.exists(caminho):
    with open(caminho, encoding="utf-8") as f:
        texto = f.read()
    novo = re.sub(r"(Última atualização: )(?:\d{2}/\d{2}/\d{4}|—)", rf"\g<1>{hoje}", texto)
    if novo != texto:
        with open(caminho, "w", encoding="utf-8", newline="") as f:
            f.write(novo)
