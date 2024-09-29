-- 1378. Replace Employee ID With The Unique Identifier
-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/?envType=study-plan-v2&envId=top-sql-50

SELECT 
    (SELECT EmployeeUNI.unique_id
    FROM EmployeeUNI
    WHERE EmployeeUNI.id = Employees.id)
    AS unique_id, Employees.name
FROM Employees;