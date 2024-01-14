## 1873. Calculate Special Bonus

Table: Employees

+-------------+---------+</br>
| Column Name | Type |</br>
+-------------+---------+</br>
| employee_id | int |</br>
| name | varchar | </br>
| salary | int | </br>
+-------------+---------+</br>

employee_id is the primary key (column with unique values) for this table.
Each row of this table indicates the employee ID, employee name, and salary.

Write a solution to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

Return the result table ordered by employee_id.

The result format is in the following example.

### Example 1:

Input:

Employees table:</br>
+-------------+---------+--------+</br>
| employee_id | name | salary |</br>
+-------------+---------+--------+</br>
| 2 | Meir | 3000 |</br>
| 3 | Michael | 3800 |</br>
| 7 | Addilyn | 7400 |</br>
| 8 | Juan | 6100 |</br>
| 9 | Kannon | 7700 |</br>
+-------------+---------+--------+</br>

Output:</br>

+-------------+-------+</br>
| employee_id | bonus |</br>
+-------------+-------+</br>
| 2 | 0 |</br>
| 3 | 0 |</br>
| 7 | 7400 |</br>
| 8 | 0 |</br>
| 9 | 7700 |</br>
+-------------+-------+

Explanation:</br>
The employees with IDs 2 and 8 get 0 bonus because they have an even employee_id.</br>
The employee with ID 3 gets 0 bonus because their name starts with 'M'.</br>
The rest of the employees get a 100% bonus.</br>
