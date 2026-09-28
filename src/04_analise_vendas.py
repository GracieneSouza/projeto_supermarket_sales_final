from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
ARQUIVO_CLEAN = BASE_DIR / "data" / "processed" / "supermarket_sales_clean.csv"
SAIDA = BASE_DIR / "resultados" / "estatisticas"
SAIDA.mkdir(parents=True, exist_ok=True)

def main():
    df = pd.read_csv(ARQUIVO_CLEAN)
    df["Date"] = pd.to_datetime(df["Date"])

    resultados = []

    branch = (
        df.groupby("Branch")
        .agg(quantidade_vendas=("Invoice ID", "count"), faturamento=("Sales", "sum"))
        .sort_values("faturamento", ascending=False)
    )
    resultados.append(["1", "Maior faturamento por filial", branch.index[0], branch.iloc[0]["faturamento"]])

    qtd = df["Branch"].value_counts()
    resultados.append(["2", "Maior quantidade de vendas por filial", qtd.index[0], qtd.iloc[0]])

    prod = (
        df.groupby("Product line")["Sales"].sum()
        .sort_values(ascending=False)
    )
    resultados.append(["3", "Maior faturamento por linha de produto", prod.index[0], prod.iloc[0]])

    rating = (
        df.groupby("Product line")["Rating"].mean()
        .sort_values(ascending=False)
    )
    resultados.append(["4", "Melhor avaliação média", rating.index[0], rating.iloc[0]])

    payment = df["Payment"].value_counts()
    resultados.append(["5", "Meio de pagamento mais utilizado", payment.index[0], payment.iloc[0]])

    resultados.append(["6", "Valor médio das vendas", "Ticket médio", df["Sales"].mean()])

    maior = df.loc[df["Sales"].idxmax()]
    resultados.append(["7", "Maior venda realizada", maior["Invoice ID"], maior["Sales"]])

    dow = df["Date"].dt.day_name().value_counts()
    resultados.append(["8", "Dia com maior quantidade de vendas", dow.index[0], dow.iloc[0]])

    out = pd.DataFrame(resultados, columns=["pergunta", "indicador", "resultado", "valor"])
    out.to_csv(SAIDA / "respostas_8_perguntas.csv", index=False)

    print("=== RESPOSTAS DAS 8 PERGUNTAS ===")
    print(out.to_string(index=False))

if __name__ == "__main__":
    main()
