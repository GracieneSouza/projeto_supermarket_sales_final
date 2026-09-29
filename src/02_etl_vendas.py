import os
import pandas as pd

# Caminhos
ARQUIVO_RAW = "SuperMarket Analysis.csv"
ARQUIVO_CLEAN = "supermarket_sales_clean.csv"

def executar_etl():
    if not os.path.exists(ARQUIVO_RAW):
        print(f"[ERRO] Ficheiro RAW '{ARQUIVO_RAW}' não encontrado.")
        return

    print("=== INICIANDO ETAPA DE ETL (TRATAMENTO E VALIDAÇÃO) ===")
    
    # 1. Carregamento do CSV RAW
    df = pd.read_csv(ARQUIVO_RAW)
    print(f"[1/5] Dados carregados: {df.shape[0]} linhas e {df.shape[1]} colunas.")

    # 2. Conversão Flexível de Tipos (Data e Hora)
    df['Date'] = pd.to_datetime(df['Date'], format='mixed').dt.date
    # Converte o horário ajustando automaticamente diferentes formatos
    df['Time'] = pd.to_datetime(df['Time'], format='mixed').dt.strftime('%H:%M')
    print("[2/5] Conversão de tipos de Data e Hora realizada.")

    # 3. Validação e Tratamento de Nulos / Valores Inválidos
    colunas_numericas_zerar = ['Quantity', 'Unit price', 'Tax 5%', 'Total', 'cogs', 'gross income']
    for col in colunas_numericas_zerar:
        if col in df.columns:
            df[col] = df[col].fillna(0)
            df.loc[df[col] < 0, col] = 0

    if 'Rating' in df.columns:
        df['Rating'] = df['Rating'].fillna(0)
        df.loc[(df['Rating'] < 1) | (df['Rating'] > 10), 'Rating'] = 0

    print("[3/5] Validação de valores numéricos e campos críticos concluída.")

    # 4. Adição de colunas auxiliares úteis para análise
    df_data_dt = pd.to_datetime(df['Date'])
    df['Year'] = df_data_dt.dt.year
    df['Month'] = df_data_dt.dt.month
    df['Month_Name'] = df_data_dt.dt.strftime('%B')
    df['Day_of_Week'] = df_data_dt.dt.day_name()
    print("[4/5] Colunas temporais auxiliares geradas (Ano, Mês, Dia da semana).")

    # 5. Guardar ficheiro tratado (Camada CLEAN)
    df.to_csv(ARQUIVO_CLEAN, index=False)
    print(f"[5/5] Ficheiro limpo salvo com sucesso em: '{ARQUIVO_CLEAN}'")
    print("=" * 55)

if __name__ == "__main__":
    executar_etl()