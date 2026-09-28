from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
ARQUIVO_CLEAN = BASE_DIR / "data" / "processed" / "supermarket_sales_clean.csv"
SAIDA = BASE_DIR / "resultados" / "relatorio_vendas_final.xlsx"

def main():
    df = pd.read_csv(ARQUIVO_CLEAN)
    df["Date"] = pd.to_datetime(df["Date"])

    branch = (
        df.groupby("Branch")
        .agg(
            quantidade_vendas=("Invoice ID", "count"),
            faturamento=("Sales", "sum"),
            ticket_medio=("Sales", "mean"),
            gross_income=("gross income", "sum"),
        )
        .sort_values("faturamento", ascending=False)
        .reset_index()
    )

    product = (
        df.groupby("Product line")
        .agg(
            quantidade_vendas=("Invoice ID", "count"),
            faturamento=("Sales", "sum"),
            ticket_medio=("Sales", "mean"),
            avaliacao_media=("Rating", "mean"),
            gross_income=("gross income", "sum"),
        )
        .sort_values("faturamento", ascending=False)
        .reset_index()
    )

    payment = (
        df["Payment"].value_counts()
        .rename_axis("meio_pagamento")
        .reset_index(name="quantidade_vendas")
    )
    payment["percentual_vendas"] = payment["quantidade_vendas"] / len(df) * 100

    dow_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    dow = (
        df["Date"].dt.day_name().value_counts()
        .reindex(dow_order)
        .fillna(0)
        .astype(int)
        .rename_axis("dia_semana")
        .reset_index(name="quantidade_vendas")
    )

    maior = df.loc[[df["Sales"].idxmax()], ["Invoice ID","Date","Branch","Product line","Sales"]].copy()

    resumo = pd.DataFrame({
        "indicador": [
            "Total de vendas", "Faturamento total", "Ticket médio",
            "Gross income total", "Maior venda",
            "Filial com maior faturamento",
            "Linha com maior faturamento",
            "Melhor avaliação média",
            "Meio de pagamento mais utilizado",
            "Dia com mais vendas"
        ],
        "valor": [
            len(df), df["Sales"].sum(), df["Sales"].mean(),
            df["gross income"].sum(), df["Sales"].max(),
            branch.iloc[0]["Branch"], product.iloc[0]["Product line"],
            product.sort_values("avaliacao_media", ascending=False).iloc[0]["Product line"],
            payment.iloc[0]["meio_pagamento"],
            dow.sort_values("quantidade_vendas", ascending=False).iloc[0]["dia_semana"]
        ]
    })

    with pd.ExcelWriter(SAIDA, engine="openpyxl") as writer:
        resumo.to_excel(writer, sheet_name="Resumo", index=False)
        branch.to_excel(writer, sheet_name="Por Filial", index=False)
        product.to_excel(writer, sheet_name="Por Produto", index=False)
        payment.to_excel(writer, sheet_name="Pagamentos", index=False)
        dow.to_excel(writer, sheet_name="Dia da Semana", index=False)
        maior.to_excel(writer, sheet_name="Maior Venda", index=False)

    print(f"[OK] Relatório criado: {SAIDA}")

if __name__ == "__main__":
    main()
