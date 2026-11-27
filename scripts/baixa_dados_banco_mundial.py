"""Baixa do Banco Mundial os dados usados no enriquecimento do capítulo de
segmentação de mercados (consumo de bebidas).

Indicadores, todos para o ano de referência da base da OMS (2010):

- SP.POP.TOTL      população total;
- SP.POP.0014.TO   população de 0 a 14 anos (para obter a população de 15 anos
                   ou mais, a mesma base do consumo per capita da OMS);
- NY.GDP.PCAP.PP.KD  PIB per capita em paridade de poder de compra (PPC),
                   em dólares internacionais constantes.

Também baixa a região e a faixa de renda de cada país. Os agregados (regiões,
grupos de renda, "Mundo" etc.) são descartados.

O arquivo é gravado em data/banco_mundial_2010.csv. Não usa bibliotecas além
do pandas. Uso, a partir da raiz do projeto:

    python scripts/baixa_dados_banco_mundial.py
"""

import json
import time
import urllib.request
from pathlib import Path

import pandas as pd

ANO = 2010
API = "https://api.worldbank.org/v2"
INDICADORES = {
    "SP.POP.TOTL": "populacao",
    "SP.POP.0014.TO": "populacao_0a14",
    "NY.GDP.PCAP.PP.KD": "pib_per_capita_ppc",
}
SAIDA = Path(__file__).resolve().parents[1] / "data" / f"banco_mundial_{ANO}.csv"


def baixa_json(url, tentativas=4):
    """Baixa uma URL da API e devolve a lista de registros (2º elemento)."""
    pedido = urllib.request.Request(url, headers={"User-Agent": "livro-aplicacoes-ds"})
    for tentativa in range(1, tentativas + 1):
        try:
            with urllib.request.urlopen(pedido, timeout=60) as resposta:
                conteudo = json.load(resposta)
            if len(conteudo) < 2 or conteudo[1] is None:
                raise ValueError(f"resposta sem dados: {conteudo[0]}")
            return conteudo[1]
        except Exception as erro:  # noqa: BLE001 - qualquer falha de rede: tenta de novo
            if tentativa == tentativas:
                raise
            print(f"  falhou ({erro}); tentando de novo...")
            time.sleep(5 * tentativa)


def baixa_paises():
    """Metadados dos países: código ISO de 3 letras, nome, região e renda."""
    registros = baixa_json(f"{API}/country?format=json&per_page=500")
    paises = pd.DataFrame(
        {
            "iso3": r["id"],
            "pais_bm": r["name"],
            "regiao": r["region"]["value"].strip(),
            "faixa_renda": r["incomeLevel"]["value"].strip(),
        }
        for r in registros
    )
    # os agregados têm região "Aggregates"
    return paises[paises["regiao"] != "Aggregates"]


def baixa_indicador(codigo, nome):
    url = f"{API}/country/all/indicator/{codigo}?date={ANO}&format=json&per_page=20000"
    registros = baixa_json(url)
    return pd.DataFrame(
        {"iso3": r["countryiso3code"], nome: r["value"]}
        for r in registros
        if r["countryiso3code"]
    )


def main():
    print("Baixando a lista de países...")
    dados = baixa_paises()

    for codigo, nome in INDICADORES.items():
        print(f"Baixando {codigo}...")
        dados = dados.merge(baixa_indicador(codigo, nome), on="iso3", how="left")

    dados["populacao_15mais"] = dados["populacao"] - dados["populacao_0a14"]
    for col in ["populacao", "populacao_15mais"]:
        dados[col] = dados[col].round().astype("Int64")
    dados["pib_per_capita_ppc"] = dados["pib_per_capita_ppc"].round().astype("Int64")
    dados = dados[["iso3", "pais_bm", "regiao", "faixa_renda",
                   "populacao", "populacao_15mais", "pib_per_capita_ppc"]]

    dados = dados.sort_values("iso3").reset_index(drop=True)
    SAIDA.parent.mkdir(exist_ok=True)
    dados.to_csv(SAIDA, index=False)

    print(f"{len(dados)} países gravados em {SAIDA}")
    print("Sem população:", dados["populacao"].isna().sum(),
          "| sem PIB per capita:", dados["pib_per_capita_ppc"].isna().sum())


if __name__ == "__main__":
    main()
