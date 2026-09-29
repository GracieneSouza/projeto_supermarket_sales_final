## O que foi encontrado no pacote enviado

O projeto estava funcional, mas havia pontos importantes de consistência que precisavam de correção:

1. `03_estatistica_vendas.py` estava usando `gross income` como se fosse faturamento. O faturamento do dataset é a coluna `Sales`.
2. `04_analise_sql.py` e `05_exportar_relatorio.py` estavam executando SQL em SQLite em memória, apesar de o projeto utilizar PostgreSQL. Além disso, essas consultas não correspondiam às oito perguntas oficiais.
3. `06_dashboard_vendas.py` utilizava `gross income` nos gráficos de desempenho e misturava `City` com `Branch`. Isso poderia apresentar gross income como faturamento e cidade como filial.
4. `03_analise.sql` continha somente a consulta do dia da semana, não as oito consultas oficiais.
5. `tratamento_supermarket_sales.sql.sql` continha somente uma validação de `Quantity`.
6. O README informava Python 3.12, enquanto o ambiente verificado no VS Code é Python 3.14.3.
7. O README dizia que o ETL removia duplicados, mas o script original não removia duplicados.
8. Não havia uma estrutura final separando claramente `data/raw`, `data/processed`, `sql`, `src` e `resultados`.
9. A base CSV anexada foi recalculada como fonte de verdade para os valores finais.

## Validação da fonte

O `SuperMarket Analysis.csv` enviado contém:

- 1.000 registros;
- 17 colunas;
- nenhum valor nulo;
- nenhuma linha duplicada;
- nenhuma quantidade <= 0;
- nenhum preço unitário <= 0;
- nenhum Sales <= 0;
- nenhum Tax 5% <= 0;
- nenhum cogs <= 0;
- nenhuma margem fora de 0–100%;
- nenhum gross income negativo;
- nenhuma avaliação fora de 1–10.

## Valores finais recalculados diretamente do CSV

- Faturamento total: 322.966,75
- Gross income total: 15.379,37
- Ticket médio: 322,97
- Mediana: 253,85
- Desvio padrão: 245,89
- Maior venda: 1.042,65

### Oito perguntas

1. Maior faturamento por filial: Giza — 110.568,71
2. Maior quantidade de vendas: Alex — 340
3. Maior faturamento por linha de produto: Food and beverages — 56.144,84
4. Melhor avaliação média: Food and beverages — 7,11
5. Meio de pagamento mais utilizado: Ewallet — 345 vendas (34,50%)
6. Valor médio das vendas: 322,97
7. Maior venda: Invoice 860-79-0874 — 1.042,65
8. Dia com maior quantidade de vendas: Saturday — 164

## Decisão metodológica

Os valores monetários acima foram recalculados diretamente do arquivo `SuperMarket Analysis.csv` presente no pacote enviado. Isso é importante porque alguns números apresentados anteriormente no desenvolvimento diferiam ligeiramente do arquivo-fonte.

O projeto final deve considerar o CSV como fonte de verdade e usar `Sales` para faturamento. `gross income` deve permanecer como indicador separado.

## Situação após a correção

Os scripts finais foram reorganizados e executados com retorno de código 0:

- `01_leitura_dados.py` — OK
- `02_etl_vendas.py` — OK
- `03_estatistica_vendas.py` — OK
- `04_analise_vendas.py` — OK
- `05_exportar_relatorio.py` — OK
- `06_dashboard_vendas.py` — OK

Os gráficos foram separados por indicador e o relatório Excel foi reconstruído com abas de resumo, filial, produto, pagamento, dia da semana e maior venda.
