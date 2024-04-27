-- 코드를 입력하세요
SELECT
	user_id,
    product_id
FROM ONLINE_SALE
GROUP BY user_id, product_id
HAVING count(*) >= 2
ORDER BY user_id, product_id desc

