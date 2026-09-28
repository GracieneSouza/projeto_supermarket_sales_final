-- Projeto Supermarket Sales
-- Validações sobre a tabela clean.sales.
-- A coluna de faturamento original do CSV é "Sales".

SELECT COUNT(*) AS total_registros
FROM clean.sales;

SELECT
    COUNT(*) FILTER (WHERE "Quantity" <= 0) AS quantidade_invalida,
    COUNT(*) FILTER (WHERE "Unit price" <= 0) AS preco_invalido,
    COUNT(*) FILTER (WHERE "Sales" <= 0) AS vendas_invalidas,
    COUNT(*) FILTER (WHERE "Tax 5%" <= 0) AS imposto_invalido,
    COUNT(*) FILTER (WHERE "cogs" <= 0) AS cogs_invalido,
    COUNT(*) FILTER (WHERE "gross income" < 0) AS gross_income_negativo,
    COUNT(*) FILTER (
        WHERE "gross margin percentage" < 0
           OR "gross margin percentage" > 100
    ) AS margem_invalida,
    COUNT(*) FILTER (
        WHERE "Rating" < 1 OR "Rating" > 10
    ) AS rating_invalido
FROM clean.sales;
