WITH LastPrices AS (
    SELECT product_id, new_price, change_date,
           ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rn
    FROM Products
    WHERE change_date <= '2019-08-16'
)
SELECT product_id, 
       COALESCE(new_price, 10) AS price
FROM (
    SELECT product_id, new_price
    FROM LastPrices
    WHERE rn = 1
    UNION
    SELECT DISTINCT product_id, 10
    FROM Products
    WHERE product_id NOT IN (SELECT product_id FROM LastPrices WHERE rn = 1)
) AS FinalPrices
ORDER BY product_id;

