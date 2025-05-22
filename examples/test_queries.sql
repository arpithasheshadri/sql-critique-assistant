-- 1. Basic SELECT *
SELECT * FROM users;

-- 2. SELECT specific columns (good style)
SELECT id, name, email FROM users;

-- 3. JOIN without aliases (style warning)
SELECT users.name, orders.amount
FROM users
JOIN orders ON users.id = orders.user_id;

-- 4. JOIN with aliases (good style)
SELECT u.name, o.amount
FROM users u
JOIN orders o ON u.id = o.user_id;

-- 5. GROUP BY without aggregate explanation
SELECT department, COUNT(*) FROM employees GROUP BY department;

-- 6. Subquery in WHERE clause (can be rewritten using CTE)
SELECT name FROM users WHERE id IN (
    SELECT user_id FROM orders WHERE amount > 100
);

-- 7. Recursive CTE (advanced)
WITH RECURSIVE numbers AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1 FROM numbers WHERE n < 10
)
SELECT * FROM numbers;

-- 8. CTE with GROUP BY (positive pattern)
WITH recent_orders AS (
    SELECT * FROM orders WHERE order_date >= '2024-01-01'
)
SELECT user_id, COUNT(*) FROM recent_orders GROUP BY user_id;

-- 9. UPDATE without WHERE (critical warning)
UPDATE users SET status = 'inactive';

-- 10. DELETE without WHERE (critical warning)
DELETE FROM users;

-- 11. ORDER BY without index (performance warning)
SELECT * FROM orders ORDER BY order_date;

-- 12. SELECT with DISTINCT that might be unnecessary
SELECT DISTINCT name FROM users WHERE age > 18;

-- 13. SELECT with redundant WHERE clause
SELECT * FROM products WHERE price > 0 AND price > 10;

-- 14. SELECT with GROUP BY but no HAVING
SELECT department_id, AVG(salary) FROM employees GROUP BY department_id;

-- 15. HAVING used instead of WHERE (logic issue)
SELECT name FROM users HAVING age > 25;

-- 16. SELECT with function use and alias (good practice)
SELECT UPPER(name) AS upper_name FROM users;

-- 17. Window function example (praiseworthy)
SELECT user_id, order_date,
       RANK() OVER (PARTITION BY user_id ORDER BY order_date DESC) AS rank
FROM orders;

-- 18. Query using BETWEEN for date range
SELECT * FROM orders WHERE order_date BETWEEN '2024-01-01' AND '2024-01-31';

-- 19. Nested SELECT with JOIN inside (can suggest flattening)
SELECT u.name FROM users u
WHERE u.id IN (
    SELECT o.user_id FROM orders o
    JOIN products p ON o.product_id = p.id
    WHERE p.price > 100
);

-- 20. SELECT using LIMIT and OFFSET (pagination pattern)
SELECT * FROM users ORDER BY created_at DESC LIMIT 10 OFFSET 20;

-- 21. IN with long static list (can suggest temp table or join)
SELECT * FROM users WHERE id IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

-- 22. Misuse of COUNT(*) vs COUNT(column)
SELECT COUNT(*) FROM orders;
SELECT COUNT(shipping_date) FROM orders;

-- 23. Non-sargable WHERE clause (poor index usage)
SELECT * FROM orders WHERE YEAR(order_date) = 2023;

-- 24. Column alias not used in ORDER BY (readability issue)
SELECT first_name AS name FROM users ORDER BY first_name;

-- 25. Use of NATURAL JOIN (style + ambiguity)
SELECT * FROM customers NATURAL JOIN orders;
