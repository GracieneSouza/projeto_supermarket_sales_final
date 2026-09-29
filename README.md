# Projeto Supermarket Sales

Projeto de análise de vendas desenvolvido com **Python, Pandas, PostgreSQL, SQL e visualização de dados** a partir do dataset `SuperMarket Analysis.csv`.

## Dashboard Executivo

[Dashboard Executivo](resultados/dashboard_vendas_executivo.png)

O dashboard apresenta os principais indicadores e resultados da análise das vendas, permitindo uma visão geral do desempenho por período, filial, linha de produto e demais dimensões analisadas.


## Objetivo

Realizar inspeção, tratamento, validação, análise estatística e análise de negócio de 1.000 vendas de uma rede de supermercados, respondendo oito perguntas definidas para o projeto.

## Tecnologias

- Python 3.12
- Pandas
- NumPy
- Matplotlib
- PostgreSQL / SQL
- OpenPyXL
- Git/GitHub

## Fluxo

`CSV → RAW → validação/ETL → CLEAN → SQL → Python → estatística → visualização → relatório`

## Perguntas de negócio

1. Qual filial possui o maior faturamento?
2. Qual filial possui a maior quantidade de vendas?
3. Qual linha de produto possui o maior faturamento?
4. Qual linha de produto possui a melhor avaliação média?
5. Qual é o meio de pagamento mais utilizado?
6. Qual é o valor médio das vendas?
7. Qual foi a maior venda realizada?
8. Qual dia da semana possui a maior quantidade de vendas?

## Resultados

| Pergunta | Resultado |
|---|---|
| Maior faturamento por filial | **Giza — 110.568,71** |
| Maior quantidade de vendas | **Alex — 340 vendas** |
| Maior faturamento por produto | **Food and beverages — 56.144,84** |
| Melhor avaliação média | **Food and beverages — 7,11** |
| Meio de pagamento mais utilizado | **E-wallet — 345 vendas (34,50%)** |
| Valor médio das vendas | **322,97** |
| Maior venda | **1.042,65** |
| Dia com mais vendas | **Sábado — 164 vendas** |

### Indicadores gerais

- Total de vendas: **1.000**
- Faturamento total: **322.966,75**
- Gross income total: **15.379,37**
- Ticket médio: **322,97**
- Mediana das vendas: **253,85**
- Desvio padrão das vendas: **245,89**

## Tratamento e validação

A base original foi preservada na camada `data/raw`.

Foram validados:

- valores nulos;
- quantidades;
- preços unitários;
- impostos;
- faturamento;
- custo de mercadorias;
- margem;
- gross income;
- avaliações;
- duplicidades.

Na base analisada não foram encontrados problemas que exigissem substituição de valores. O ETL realiza a conversão dos campos de data e hora e acrescenta variáveis temporais para análise.

## Estrutura

```text
projeto_supermarket_sales_final/
├── data/
├── src/
│   ├── 01_leitura_dados.py
│   ├── 02_etl_vendas.py
│   ├── 03_estatistica_vendas.py
│   ├── 04_analise_vendas.py
│   ├── 05_exportar_relatorio.py
│   └── 06_dashboard_vendas.py
├── sql/
│   ├── 01_validacao.sql
│   ├── 02_analise.sql
│   └── 03_tratamento_validacao.sql
├── resultados/
│   ├── estatisticas/
│   ├── graficos/
│   ├── dashboard_vendas_executivo.png
│   └── relatorio_vendas_final.xlsx
├── .gitignore
├── AUDITORIA_FINAL.md
├── README.md
└── requirements.txt
```

## Execução

Na raiz do projeto:

```bash
python src/01_leitura_dados.py
python src/02_etl_vendas.py
python src/03_estatistica_vendas.py
python src/04_analise_vendas.py
python src/05_exportar_relatorio.py
python src/06_dashboard_vendas.py
```

As consultas PostgreSQL estão em `sql/02_analise.sql`.

## Observação metodológica

No dataset original, a coluna de faturamento é `Sales`. Ela não deve ser confundida com `gross income`: `gross income` representa uma medida diferente e não deve ser usada como sinônimo de faturamento.

Os resultados apresentados neste README foram calculados a partir do dataset SuperMarket Analysis.csv utilizado localmente no projeto. Os arquivos de dados brutos e processados não são versionados no repositório.
