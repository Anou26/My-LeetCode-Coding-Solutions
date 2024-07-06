WITH daily_totals AS (
    SELECT 
        visited_on,
        SUM(amount) AS daily_total
    FROM 
        Customer
    GROUP BY 
        visited_on
),
window_sums AS (
    SELECT 
        visited_on,
        SUM(daily_total) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS window_sum,
        COUNT(daily_total) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS window_count
    FROM 
        daily_totals
)
SELECT 
    visited_on,
    window_sum AS amount,
    ROUND(window_sum / window_count, 2) AS average_amount
FROM 
    window_sums
WHERE 
    window_count = 7
ORDER BY 
    visited_on;
