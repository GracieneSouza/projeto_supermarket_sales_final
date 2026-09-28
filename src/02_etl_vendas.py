from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]

ARQUIVO_RAW = BASE_DIR / "data" / "raw" / "SuperMarket Analysis.csv"
ARQUIVO_CLEAN = BASE_DIR / "data" / "processed" / "supermarket_sales_clean.csv"


NUMERICOS = [
    "Unit price",
    "Quantity",
    "Tax 5%",
    "Sales",
    "cogs",
    "gross margin percentage",
    "gross income",
    "Rating",
    
]


def validar(df):
    erros = []

    # Valores nulos
    if df.isna().any().any():
        erros.append("Existem valores nulos.")

    # Quantidade
    if (df["Quantity"] <= 0).any():
        erros.append("Existem quantidades menores ou iguais a zero.")

    # Preço unitário
    if (df["Unit price"] <= 0).any():
        erros.append("Existem preços unitários menores ou iguais a zero.")

    # Imposto
    if (df["Tax 5%"] <= 0).any():
        erros.append("Existem valores de Tax 5% menores ou iguais a zero.")

    # Sales
    if (df["Sales"] <= 0).any():
        erros.append("Existem valores de Sales menores ou iguais a zero.")

    # Custo das mercadorias
    if (df["cogs"] <= 0).any():
        erros.append("Existem valores de cogs menores ou iguais a zero.")

    # Margem
    if (
        (df["gross margin percentage"] < 0)
        | (df["gross margin percentage"] > 100)
    ).any():
        erros.append("Existem margens fora do intervalo de 0 a 100.")

    # Receita bruta
    if (df["gross income"] < 0).any():
        erros.append("Existem valores negativos de gross income.")

   # Avaliação
    if (
        (df["Rating"] < 1)
        | (df["Rating"] > 10)
    ).any():
        erros.append("Existem avaliações fora do intervalo de 1 a 10.")

    # Duplicidades
    if df.duplicated().any():
        erros.append("Existem linhas duplicadas.")

    return erros


def main():

    # Leitura da base RAW
    df = pd.read_csv(ARQUIVO_RAW)

    # Conversão de tipos
    df["Date"] = pd.to_datetime(
        df["Date"],
        format="mixed"
    )

    df["Time"] = pd.to_datetime(
        df["Time"],
        format="mixed"
    ).dt.time

    # Garantia dos tipos numéricos
    for col in NUMERICOS:
        df[col] = pd.to_numeric(
            df[col],
            errors="raise"
        )

    # Validação
    erros = validar(df)

    if erros:
        raise ValueError(
            "Validação interrompida:\n- "
            + "\n- ".join(erros)
        )

    # Colunas auxiliares para análise
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Month_Name"] = df["Date"].dt.strftime("%B")
    df["Day_of_Week"] = df["Date"].dt.day_name()

    # Formatação para CSV
    df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
    df["Time"] = df["Time"].astype(str)

    # Exportação da base CLEAN
    df.to_csv(
        ARQUIVO_CLEAN,
        index=False
    )

    print("=== ETL E VALIDAÇÃO CONCLUÍDOS ===")
    print(f"Registros: {len(df)}")
    print(f"Colunas: {len(df.columns)}")
    print(f"Arquivo CLEAN: {ARQUIVO_CLEAN}")
    print("Resultado da validação: nenhum problema encontrado.")


if __name__ == "__main__":
    main()