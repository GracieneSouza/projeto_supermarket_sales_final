-- Projeto Supermarket Sales
-- As oito perguntas oficiais do projeto.

-- 1. Qual filial possui o maior faturamento?
SELECT
    "Branch" AS filial,
    COUNT(*) AS quantidade_vendas,
    ROUND(SUM("Sales")::numeric, 2) AS faturamento,
    ROUND(AVG("Sales")::numeric, 2) AS ticket_medio
ORDER BY faturamento DESC;

-- 2. Qual filial possui a maior quantidade de vendas?
SELECT
    "Branch" AS filial,
    COUNT(*) AS quantidade_vendas
FROM clean.sales
GROUP BY "Branch"
ORDER BY quantidade_vendas DESC;

-- 3. Qual linha de produto possui o maior faturamento?
SELECT
    "Product line" AS linha_produto,
    COUNT(*) AS quantidade_vendas,
    ROUND(SUM("Sales")::numeric, 2) AS faturamento
FROM clean.sales
GROUP BY "Product line"
ORDER BY faturamento DESC;

-- 4. Qual linha de produto possui a melhor avaliação média?
SELECT
    "Product line" AS linha_produto,
    ROUND(AVG("Rating")::numeric, 2) AS avaliacao_media
FROM clean.sales
GROUP BY "Product line"
ORDER BY avaliacao_media DESC;

-- 5. Qual é o meio de pagamento mais utilizado?
SELECT
    "Payment" AS meio_pagamento,
    COUNT(*) AS quantidade_vendas,
    ROUND((COUNT(*) * 100.0 / SUM(COUNT(*)) OVER ())::numeric, 2) AS percentual
FROM clean.sales
GROUP BY "Payment"
ORDER BY quantidade_vendas DESC;

-- 6. Qual é o valor médio das vendas?
SELECT ROUND(AVG("Sales")::numeric, 2) AS ticket_medio
FROM clean.sales;

-- 7. Qual foi a maior venda realizada?
SELECT
    "Invoice ID",
    "Date",
    "Branch",
    "Product line",
    ROUND("Sales"::numeric, 2) AS valor_venda
FROM clean.sales
ORDER BY "Sales" DESC
LIMIT 1;

-- 8. Qual dia da semana possui a maior quantidade de vendas?
SELECT
    TRIM(TO_CHAR("Date", 'Day')) AS dia_semana,
    COUNT(*) AS quantidade_vendas
FROM clean.sales
GROUP BY TRIM(TO_CHAR("Date", 'Day'))
ORDER BY quantidade_vendas DESC;
