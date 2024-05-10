# Write your MySQL query statement below
/*
SELECT
MONTH(trans_date) as month,
country, COUNT(trans_count),
COUNT(IF state == "approved", THEN 1 ELSE 0)
SUM(amount) as approved_total_amount
FROM Transactions
GROUP BY month
*/
SELECT
    DATE_FORMAT(trans_date, '%Y-%m') as month,
    country,
    COUNT(id) as trans_count,
    SUM(state = 'approved') as approved_count,
    SUM(amount) as trans_total_amount,
    SUM(IF(state = 'approved', amount, 0)) as approved_total_amount
FROM Transactions
GROUP BY month, country