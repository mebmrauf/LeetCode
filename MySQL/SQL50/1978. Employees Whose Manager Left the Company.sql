-- 1978. Employees Whose Manager Left the Company
-- https://leetcode.com/problems/employees-whose-manager-left-the-company/description/?envType=study-plan-v2&envId=top-sql-50

SELECT Employees.employee_id
FROM Employees
WHERE Employees.salary < 30000 AND Employees.manager_id IS NOT NULL AND Employees.manager_id NOT IN
(SELECT employee_id FROM Employees)
ORDER BY Employees.employee_id;