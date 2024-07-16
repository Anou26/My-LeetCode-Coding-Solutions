# Write your MySQL query statement below
WITH RankedSalaries AS (
    SELECT
        D.name AS Department,
        E.name AS Employee,
        E.salary,
        DENSE_RANK() OVER (PARTITION BY E.departmentId ORDER BY E.salary DESC) AS salary_rank
    FROM
        Employee E
    JOIN
        Department D ON E.departmentId = D.id
)
SELECT
    Department,
    Employee,
    salary AS Salary
FROM
    RankedSalaries
WHERE
    salary_rank <= 3
ORDER BY
    Department, Salary DESC;
