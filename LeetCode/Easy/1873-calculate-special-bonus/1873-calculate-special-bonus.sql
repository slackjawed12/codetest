SELECT
  employee_id,
  IF(employee_id % 2 = 1 AND (name REGEXP '^M+')<1, salary, 0) AS bonus
FROM
  Employees
ORDER BY
  employee_id
