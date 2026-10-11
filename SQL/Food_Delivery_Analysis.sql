CREATE DATABASE IF NOT EXISTS food_delivery_db;

USE food_delivery_db;

ALTER TABLE cleaned_food_delivery  RENAME TO orders;

SELECT *
FROM orders
LIMIT 10;

SELECT COUNT(*) AS total_orders
FROM orders;

SELECT
    restaurant_name,
    COUNT(*) AS total_orders,
    SUM(total_amount) AS total_sales
FROM orders
WHERE order_status = 'Delivered'
GROUP BY restaurant_name
ORDER BY total_sales DESC
LIMIT 5;


SELECT
    payment_method,
    COUNT(*) AS total_orders
FROM orders
GROUP BY payment_method
ORDER BY total_orders DESC;

SELECT
    ROUND(AVG(delivery_time_minutes), 2)
        AS average_delivery_time
FROM orders
WHERE order_status = 'Delivered';

SELECT
    city,
    COUNT(*) AS total_orders
FROM orders
GROUP BY city
ORDER BY total_orders DESC;

SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    COUNT(*) AS total_orders,
    SUM(total_amount) AS monthly_sales
FROM orders
WHERE order_status = 'Delivered'
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY month;
