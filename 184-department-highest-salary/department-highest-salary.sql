# Write your MySQL query statement below
WITH ranking AS (
    SELECT d.name as Department,e.name as Employee, e.salary as Salary, 
    RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) as salary_rank
    FROM Employee e LEFT JOIN Department d 
    ON e.departmentId=d.id
)
SELECT Department, Employee, Salary FROM ranking
WHERE salary_rank=1