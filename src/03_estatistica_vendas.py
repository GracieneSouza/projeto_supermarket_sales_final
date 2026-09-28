from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
ARQUIVO_CLEAN = BASE_DIR / "data" / "processed" / "supermarket_sales_clean.csv"
SAIDA = BASE_DIR / "resultados" / "estatisticas"
SAIDA.mkdir(parents=True, exist_ok=True)

def main():
    df = pd.read_csv(ARQUIVO_CLEAN)

    print(df.columns.tolist())

    estatisticas = df["Sales"].describe().rename({
        "count": "quantidade",
        "mean": "media",
        "std": "desvio_padrao",
        "min": "minimo",
        "25%": "q1",
        "50%": "mediana",
        "75%": "q3",
        "max": "maximo",
    })

    resumo = pd.DataFrame({
        "metrica": estatisticas.index,
        "valor": estatisticas.values
    })
    resumo.to_csv(SAIDA / "estatistica_vendas.csv", index=False)

    por_produto = (
        df.groupby("Product line")
        .agg(
            quantidade_vendas=("Invoice ID", "count"),
            faturamento=("Sales", "sum"),
            ticket_medio=("Sales", "mean"),
            avaliacao_media=("Rating", "mean"),
        )
        .sort_values("faturamento", ascending=False)
        .reset_index()
    )
    por_produto.to_csv(SAIDA / "estatistica_por_produto.csv", index=False)

    print("=== ESTATÍSTICA DESCRITIVA ===")
    print(f"Faturamento : {df['Sales'].sum():.2f}")
    print(f"Ticket médio: {df['Sales'].mean():.2f}")
    print(f"Mediana: {df['Sales'].median():.2f}")
    print(f"Desvio padrão: {df['Sales'].std():.2f}")
    print(f"Maior venda: {df['Sales'].max():.2f}")

if __name__ == "__main__":
    main()
