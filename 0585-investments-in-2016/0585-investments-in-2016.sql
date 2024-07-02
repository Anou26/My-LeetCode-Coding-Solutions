# Write your MySQL query statement below
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM (
    SELECT i1.*
    FROM Insurance i1
    JOIN (
        -- Find all tiv_2015 values that are duplicated
        SELECT tiv_2015
        FROM Insurance
        GROUP BY tiv_2015
        HAVING COUNT(*) > 1
    ) dup_tiv_2015 ON i1.tiv_2015 = dup_tiv_2015.tiv_2015
    WHERE (i1.lat, i1.lon) IN (
        -- Find all (lat, lon) pairs that are unique
        SELECT lat, lon
        FROM Insurance
        GROUP BY lat, lon
        HAVING COUNT(*) = 1
    )
) subquery;
