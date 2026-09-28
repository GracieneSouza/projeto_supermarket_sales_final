-- Tratamento e validação documentados.
-- A base original não apresentou problemas de qualidade que exigissem
-- substituição de valores. Portanto, o tratamento consiste principalmente
-- na conversão de tipos e na criação da camada CLEAN.

-- Validação de nulos
SELECT
    COUNT(*) FILTER (WHERE "Invoice ID" IS NULL) AS invoice_id_nulos,
    COUNT(*) FILTER (WHERE "Branch" IS NULL) AS branch_nulos,
    COUNT(*) FILTER (WHERE "Product line" IS NULL) AS produto_nulos,
    COUNT(*) FILTER (WHERE "Sales" IS NULL) AS sales_nulos,
    COUNT(*) FILTER (WHERE "Rating" IS NULL) AS rating_nulos
FROM raw.sales;

-- Validação de valores
SELECT
    COUNT(*) FILTER (WHERE "Quantity" <= 0) AS quantity_invalida,
    COUNT(*) FILTER (WHERE "Unit price" <= 0) AS unit_price_invalido,
    COUNT(*) FILTER (WHERE "Sales" <= 0) AS sales_invalido,
    COUNT(*) FILTER (WHERE "Tax 5%" <= 0) AS tax_invalido,
    COUNT(*) FILTER (WHERE "cogs" <= 0) AS cogs_invalido,
    COUNT(*) FILTER (
        WHERE "gross margin percentage" < 0
           OR "gross margin percentage" > 100
    ) AS margem_invalida,
    COUNT(*) FILTER (WHERE "gross income" < 0) AS gross_income_invalido,
    COUNT(*) FILTER (WHERE "Rating" < 1 OR "Rating" > 10) AS rating_invalido
FROM raw.sales;

-- Verificação de duplicidades
SELECT
    COUNT(*) AS linhas_duplicadas
FROM (
    SELECT "Invoice ID"
    FROM raw.sales
    GROUP BY "Invoice ID"
    HAVING COUNT(*) > 1
) duplicadas;
