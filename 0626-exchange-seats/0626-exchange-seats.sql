SELECT 
    CASE
        WHEN MOD(s1.id, 2) = 1 AND s2.id IS NOT NULL THEN s2.id
        WHEN MOD(s1.id, 2) = 0 THEN s1.id - 1
        ELSE s1.id
    END AS id,
    s1.student
FROM 
    Seat s1
LEFT JOIN 
    Seat s2 ON s1.id = s2.id - 1
ORDER BY id;
