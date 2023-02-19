-- 코드를 입력하세요
SELECT 
    animal_id,
    name
FROM ANIMAL_INS
WHERE NAME LIKE '%el%' AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME ASC;