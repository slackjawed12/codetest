# Write your MySQL query statement below
SELECT *
FROM (
    SELECT 
        product_id,
        "store1" AS store,
        store1 AS price
    FROM
        Products as s1
    WHERE store1 IS NOT NULL

    UNION

    SELECT 
        product_id,
        "store2" AS store,
        store2 AS price
    FROM
        Products as s2
    WHERE store2 IS NOT NULL

    UNION
    
    SELECT 
        product_id,
        "store3" AS store,
        store3 AS price
    FROM
        Products as s3
    WHERE store3 IS NOT NULL
) as total