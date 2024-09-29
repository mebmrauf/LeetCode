-- 1075. Project Employees I
-- https://leetcode.com/problems/project-employees-i/?envType=study-plan-v2&envId=top-sql-50

SELECT Project.project_id, ROUND(AVG(Employee.experience_years), 2) AS average_years
FROM Project
JOIN Employee 
ON Project.employee_id = Employee.employee_id
GROUP BY Project.project_id;