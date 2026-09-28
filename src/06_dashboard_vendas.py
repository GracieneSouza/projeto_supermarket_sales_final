from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parents[1]
ARQUIVO_CLEAN = BASE_DIR / "data" / "processed" / "supermarket_sales_clean.csv"
SAIDA = BASE_DIR / "resultados" / "graficos"
SAIDA.mkdir(parents=True, exist_ok=True)

def salvar_grafico(fig, nome):
    fig.tight_layout()
    fig.savefig(SAIDA / nome, dpi=200, bbox_inches="tight")
    plt.close(fig)

def main():
    df = pd.read_csv(ARQUIVO_CLEAN)
    df["Date"] = pd.to_datetime(df["Date"])

    # 1. Faturamento por filial
    s = df.groupby("Branch")["Sales"].sum().sort_values()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(s.index, s.values)
    ax.set_title("Faturamento por Filial")
    ax.set_xlabel("Faturamento")
    salvar_grafico(fig, "01_faturamento_por_filial.png")

    # 2. Quantidade de vendas por filial
    s = df["Branch"].value_counts().sort_values()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(s.index, s.values)
    ax.set_title("Quantidade de Vendas por Filial")
    ax.set_xlabel("Quantidade de vendas")
    salvar_grafico(fig, "02_quantidade_vendas_por_filial.png")

    # 3. Faturamento por linha de produto
    s = df.groupby("Product line")["Sales"].sum().sort_values()
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.barh(s.index, s.values)
    ax.set_title("Faturamento por Linha de Produto")
    ax.set_xlabel("Faturamento")
    salvar_grafico(fig, "03_faturamento_por_produto.png")

    # 4. Avaliação média
    s = df.groupby("Product line")["Rating"].mean().sort_values()
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.barh(s.index, s.values)
    ax.set_title("Avaliação Média por Linha de Produto")
    ax.set_xlabel("Nota média")
    ax.set_xlim(0, 10)
    salvar_grafico(fig, "04_avaliacao_media_por_produto.png")

    # 5. Meios de pagamento
    s = df["Payment"].value_counts()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(s.index, s.values)
    ax.set_title("Meios de Pagamento Mais Utilizados")
    ax.set_ylabel("Quantidade de vendas")
    ax.tick_params(axis="x", rotation=15)
    salvar_grafico(fig, "05_meios_pagamento.png")

    # 6. Vendas por dia da semana
    ordem = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    s = df["Date"].dt.day_name().value_counts().reindex(ordem)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(s.index, s.values)
    ax.set_title("Quantidade de Vendas por Dia da Semana")
    ax.set_ylabel("Quantidade de vendas")
    ax.tick_params(axis="x", rotation=20)
    salvar_grafico(fig, "06_vendas_por_dia_semana.png")

    # 7. Resumo executivo em uma única página (tabela, não subplots)
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.axis("off")
    texto = (
        "PROJETO SUPERMARKET SALES\n\n"
        f"Total de vendas: {len(df):,}\n"
        f"Faturamento total: {df['Sales'].sum():,.2f}\n"
        f"Ticket médio: {df['Sales'].mean():,.2f}\n"
        f"Maior venda: {df['Sales'].max():,.2f}\n\n"
        f"Maior faturamento por filial: "
        f"{df.groupby('Branch')['Sales'].sum().idxmax()}\n"
        f"Maior faturamento por produto: "
        f"{df.groupby('Product line')['Sales'].sum().idxmax()}\n"
        f"Melhor avaliação média: "
        f"{df.groupby('Product line')['Rating'].mean().idxmax()}\n"
        f"Pagamento mais utilizado: {df['Payment'].value_counts().idxmax()}\n"
        f"Dia com mais vendas: {df['Date'].dt.day_name().value_counts().idxmax()}"
    )
    ax.text(0.05, 0.95, texto, va="top", ha="left", fontsize=16)
    fig.savefig(SAIDA / "dashboard_vendas_executivo.png", dpi=200, bbox_inches="tight")
    plt.close(fig)

    print(f"[OK] Gráficos salvos em: {SAIDA}")

if __name__ == "__main__":
    main()
