-- 코드를 입력하세요
SELECT 
warehouse_id, 
warehouse_name, 
address, 
if(freezer_yn=null, 'N', if(freezer_yn='Y', 'Y', 'N')) as freezer_yn
from food_warehouse
where left(address, 3) = '경기도'
order by warehouse_id asc;