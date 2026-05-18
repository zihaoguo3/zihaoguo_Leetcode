# Write your MySQL query statement below
WITH counting AS(SELECT customer_number, count(order_number) as ordering
FROM Orders
GROUP BY customer_number)
SELECT customer_number 
FROM counting
ORDER BY ordering DESC
LIMIT 1