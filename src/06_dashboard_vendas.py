from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Configuração de estilo geral do Matplotlib
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

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

    # Color palette
    color_main = "#2b5c8f"

    # 1. Faturamento por filial
    s = df.groupby("Branch")["Sales"].sum().sort_values()
    fig, ax = plt.subplots(figsize=(8, 4.5))
    bars = ax.barh(s.index, s.values, color=color_main)
    ax.set_title("Faturamento Total por Filial", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Faturamento ($)")
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))
    ax.bar_label(bars, fmt="${x:,.2f}", padding=5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    salvar_grafico(fig, "01_faturamento_por_filial.png")

    # 2. Quantidade de vendas por filial
    s = df["Branch"].value_counts().sort_values()
    fig, ax = plt.subplots(figsize=(8, 4.5))
    bars = ax.barh(s.index, s.values, color=color_main)
    ax.set_title("Quantidade de Transações por Filial", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Quantidade de Vendas")
    ax.bar_label(bars, padding=5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    salvar_grafico(fig, "02_quantidade_vendas_por_filial.png")

    # 3. Faturamento por linha de produto
    s = df.groupby("Product line")["Sales"].sum().sort_values()
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(s.index, s.values, color=color_main)
    ax.set_title("Faturamento por Linha de Produto", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Faturamento ($)")
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))
    ax.bar_label(bars, fmt="${x:,.2f}", padding=5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    salvar_grafico(fig, "03_faturamento_por_produto.png")

    # 4. Avaliação média
    s = df.groupby("Product line")["Rating"].mean().sort_values()
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(s.index, s.values, color="#d95f02")
    ax.set_title("Avaliação Média por Linha de Produto", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Nota Média (0 - 10)")
    ax.set_xlim(0, 10)
    ax.bar_label(bars, fmt="%.2f", padding=5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    salvar_grafico(fig, "04_avaliacao_media_por_produto.png")

    # 5. Meios de pagamento
    s = df["Payment"].value_counts()
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(s.index, s.values, color=color_main, width=0.6)
    ax.set_title("Meios de Pagamento Mais Utilizados", fontsize=14, fontweight="bold", pad=15)
    ax.set_ylabel("Quantidade de Vendas")
    ax.tick_params(axis="x", rotation=0)
    ax.bar_label(bars, padding=3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    salvar_grafico(fig, "05_meios_pagamento.png")

    # 6. Vendas por dia da semana
    ordem = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    ordem_pt = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    s = df["Date"].dt.day_name().value_counts().reindex(ordem)
    
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(ordem_pt, s.values, color=color_main, width=0.6)
    ax.set_title("Quantidade de Vendas por Dia da Semana", fontsize=14, fontweight="bold", pad=15)
    ax.set_ylabel("Quantidade de Vendas")
    ax.tick_params(axis="x", rotation=0)
    ax.bar_label(bars, padding=3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    salvar_grafico(fig, "06_vendas_por_dia_semana.png")

    # 7. Resumo executivo
    fig, ax = plt.subplots(figsize=(10, 6.5))
    ax.axis("off")
    
    # Caixa visual para o painel executivo
    ax.add_patch(plt.Rectangle((0.02, 0.02), 0.96, 0.96, fill=True, color="#f8f9fa", ec="#cccccc", lw=1.5, transform=ax.transAxes))

    faturamento_total = df['Sales'].sum()
    ticket_medio = df['Sales'].mean()
    maior_venda = df['Sales'].max()
    filial_top = df.groupby('Branch')['Sales'].sum().idxmax()
    produto_top = df.groupby('Product line')['Sales'].sum().idxmax()
    rating_top = df.groupby('Product line')['Rating'].mean().idxmax()
    pagamento_top = df['Payment'].value_counts().idxmax()
    dia_top = df['Date'].dt.day_name().value_counts().idxmax()

    texto = (
        "DASHBOARD EXECUTIVO DE VENDAS\n"
        "--------------------------------------------------\n\n"
        f"• Total de Transações:   {len(df):,}\n"
        f"• Faturamento Total:     ${faturamento_total:,.2f}\n"
        f"• Ticket Médio:          ${ticket_medio:,.2f}\n"
        f"• Maior Venda Individual: ${maior_venda:,.2f}\n\n"
        f"• Filial Líder em Vendas: {filial_top}\n"
        f"• Categoria mais Lucrativa: {produto_top}\n"
        f"• Categoria Melhor Avaliada: {rating_top}\n"
        f"• Meio de Pagamento Dominante: {pagamento_top}\n"
        f"• Dia de Maior Movimento: {dia_top}"
    )

    ax.text(0.08, 0.88, texto, va="top", ha="left", fontsize=13, fontfamily="monospace", linespacing=1.6)
    
    fig.savefig(SAIDA / "dashboard_vendas_executivo.png", dpi=200, bbox_inches="tight")
    plt.close(fig)

    print(f"[OK] Gráficos salvos com sucesso em: {SAIDA}")

if __name__ == "__main__":
    main()