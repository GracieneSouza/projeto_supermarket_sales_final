from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
ARQUIVO_RAW = BASE_DIR / "data" / "raw" / "SuperMarket Analysis.csv"

def main():
    df = pd.read_csv(ARQUIVO_RAW)

    print("=== INSPEÇÃO INICIAL DA BASE ===")
    print(f"Arquivo: {ARQUIVO_RAW}")
    print(f"Linhas: {df.shape[0]}")
    print(f"Colunas: {df.shape[1]}")
    print("\nPrimeiras linhas:")
    print(df.head().to_string(index=False))

    print("\nTipos de dados:")
    print(df.dtypes)

    print("\nValores nulos por coluna:")
    print(df.isna().sum())

    print(f"\nLinhas duplicadas: {df.duplicated().sum()}")

if __name__ == "__main__":
    main()
