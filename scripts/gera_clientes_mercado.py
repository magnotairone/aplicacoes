"""Gera a base simulada de clientes do mercado usada no capítulo de agrupamento.

A base é uma "foto" tirada em uma data de referência:

- inclui os clientes com pelo menos uma compra nos 12 meses anteriores;
- gastos e `interesse` referem-se aos 6 meses (26 semanas) anteriores;
- `dias_ult_compra` é contado até a data de referência.

O comportamento é simulado semana a semana (visitas e gasto por visita), de
modo que as variáveis sejam coerentes entre si: quem não comprou na janela de
6 meses tem gasto zero, e o gasto total é a soma das cinco categorias mais as
"outras compras" (que não estão na base).

Uso, a partir da raiz do projeto:

    python scripts/gera_clientes_mercado.py
"""

from pathlib import Path

import numpy as np
import pandas as pd

SEMENTE = 2024
N_CLIENTES = 60_000
SEMANAS = 26                 # janela de 6 meses
DIAS_JANELA = SEMANAS * 7    # 182 dias
SALARIO_MINIMO = 1_518
SAIDA = Path(__file__).resolve().parents[1] / "data" / "clientes_mercado.csv"

CATEGORIAS = ["vinho", "queijo", "cerveja", "flv", "mercearia", "outras"]

# Perfis latentes. Cada perfil tem hábitos de compra próprios (frequência,
# ticket e mix de categorias), com variação entre clientes suficiente para que
# os grupos se sobreponham em parte, como em uma base real.
PERFIS = {
    "fiel": dict(
        peso=0.18, idade=(44, 10), renda=3_900,
        visita=(30, 6),          # Beta da chance de comprar em cada semana (média 0,83)
        ticket=120,              # gasto mediano por visita, em R$
        mix=[1, 2, 3, 11, 15, 18],                 # participação de cada categoria (Dirichlet)
        compra=[0.25, 0.70, 0.55, 0.98, 0.99, 1],  # chance de o cliente comprar a categoria
        para=0.02, para_ate=26,  # chance de parar de comprar e até que semana
    ),
    "seletivo": dict(
        peso=0.24, idade=(50, 10), renda=8_000,
        visita=(16, 24), ticket=170,
        mix=[8, 5, 2, 6, 4, 15], compra=[0.85, 0.85, 0.30, 0.90, 0.70, 1],
        para=0.03, para_ate=26,
    ),
    "esporadico": dict(
        peso=0.40, idade=(35, 10), renda=3_200,
        visita=(8, 20), ticket=85,
        mix=[0.6, 0.6, 5, 3, 8, 14], compra=[0.10, 0.20, 0.55, 0.70, 0.90, 1],
        para=0.05, para_ate=26,
    ),
    "inativo": dict(
        peso=0.18, idade=(40, 12), renda=2_700,
        visita=(2, 14), ticket=60,
        mix=[0.5, 0.5, 4, 2, 7, 14], compra=[0.05, 0.10, 0.40, 0.50, 0.80, 1],
        para=1.0, para_ate=13,   # todos pararam de comprar na primeira metade da janela
    ),
}

CONCENTRACAO_MIX = 3   # quanto maior, mais parecido é o mix dos clientes de um perfil


def simula_cliente(rng, perfil):
    p = PERFIS[perfil]

    idade = int(np.clip(rng.normal(*p["idade"]), 18, 85))
    renda = max(SALARIO_MINIMO, p["renda"] * np.exp(rng.normal(0, 0.25)) * (1 + 0.004 * (idade - 40)))
    score = np.clip(480 + 110 * np.log(renda / SALARIO_MINIMO) + rng.normal(0, 90), 0, 1000)

    # semanas com visita: probabilidade semanal do cliente; alguns param de vir
    # em alguma semana da janela (clientes em processo de abandono)
    prob = rng.beta(*p["visita"])
    ultima_semana_ativa = SEMANAS
    if rng.random() < p["para"]:
        ultima_semana_ativa = rng.integers(0, p["para_ate"])  # 0 = já não veio na janela
    visitou = rng.random(SEMANAS) < prob
    visitou[ultima_semana_ativa:] = False
    semanas_com_visita = np.flatnonzero(visitou)

    n_visitas = len(semanas_com_visita)
    if n_visitas > 0:
        ultima = semanas_com_visita[-1]          # semana 25 = a mais recente
        dias_ult = (SEMANAS - 1 - ultima) * 7 + rng.integers(0, 7)
    else:
        # última compra antes da janela (base: compra nos últimos 12 meses)
        dias_ult = DIAS_JANELA + rng.integers(0, 365 - DIAS_JANELA)

    # gasto: ticket do cliente (varia com a renda) vezes ruído por visita
    ticket_cliente = p["ticket"] * np.exp(rng.normal(0, 0.25)) * (renda / p["renda"]) ** 0.3
    total = float(np.sum(ticket_cliente * rng.lognormal(0, 0.35, n_visitas)))

    # divisão do gasto entre as categorias que o cliente compra
    compra = rng.random(len(CATEGORIAS)) < np.array(p["compra"])
    compra[-1] = True  # sempre há "outras compras"
    pesos = rng.dirichlet(CONCENTRACAO_MIX * np.array(p["mix"], dtype=float)) * compra
    gastos = total * pesos / pesos.sum()

    return dict(
        idade=idade,
        renda=round(renda, 2),
        score_serasa=round(float(score), 0),
        interesse=round(n_visitas / SEMANAS, 2),
        dias_ult_compra=int(dias_ult),
        vlr_tran_total_6m=round(total, 2),
        **{f"gasto_{c}_6m": round(float(g), 2) for c, g in zip(CATEGORIAS[:-1], gastos[:-1])},
    )


def main():
    rng = np.random.default_rng(SEMENTE)
    nomes = list(PERFIS)
    pesos = np.array([PERFIS[n]["peso"] for n in nomes])
    perfis = rng.choice(nomes, size=N_CLIENTES, p=pesos / pesos.sum())

    df = pd.DataFrame([simula_cliente(rng, perfil) for perfil in perfis])

    # o arredondamento das categorias pode passar o total em alguns centavos
    cats = [f"gasto_{c}_6m" for c in CATEGORIAS[:-1]]
    excesso = (df[cats].sum(axis=1) - df["vlr_tran_total_6m"]).clip(lower=0)
    df["vlr_tran_total_6m"] = (df["vlr_tran_total_6m"] + excesso).round(2)

    SAIDA.parent.mkdir(exist_ok=True)
    df.to_csv(SAIDA, index=False)
    print(f"{len(df)} clientes gravados em {SAIDA}")


if __name__ == "__main__":
    main()
