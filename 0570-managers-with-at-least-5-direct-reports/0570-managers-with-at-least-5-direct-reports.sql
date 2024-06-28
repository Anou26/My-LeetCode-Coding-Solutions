# Write your MySQL query statement below
SELECT
    e.name
FROM
    Employee e
JOIN
    (SELECT
         managerId,
         COUNT(*) AS report_count
     FROM
         Employee
     WHERE
         managerId IS NOT NULL
     GROUP BY
         managerId
     HAVING
         COUNT(*) >= 5) sub
ON
    e.id = sub.managerId
