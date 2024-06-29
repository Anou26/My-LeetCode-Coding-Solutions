# Write your MySQL query statement below
SELECT ROUND((COUNT(CASE WHEN d.order_date = d.customer_pref_delivery_date THEN 1 END) / COUNT(DISTINCT d.customer_id)) * 100, 2) AS immediate_percentage
FROM (
    SELECT customer_id, MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
) AS first_orders
JOIN Delivery AS d ON first_orders.customer_id = d.customer_id AND first_orders.first_order_date = d.order_date;
