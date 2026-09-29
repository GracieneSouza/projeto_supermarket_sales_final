import pandas as pd

# Caminho do arquivo CSV
arquivo = "SuperMarket Analysis.csv"

# Leitura da base de dados
df = pd.read_csv(arquivo)

# Exibe as primeiras linhas
print(df.head())

# Exibe informações gerais da base
print("\nInformações da base:")
print(df.info())

# Exibe a quantidade de linhas e colunas
print("\nDimensões da base:")
print(df.shape)