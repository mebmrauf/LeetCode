-- 577. Employee Bonus
-- https://leetcode.com/problems/employee-bonus/?envType=study-plan-v2&envId=top-sql-50

SELECT Employee.name, Bonus.bonus
FROM Employee
LEFT JOIN Bonus
ON Employee.empId = Bonus.empId
WHERE Bonus.bonus < 1000 OR Bonus.bonus IS NULL;