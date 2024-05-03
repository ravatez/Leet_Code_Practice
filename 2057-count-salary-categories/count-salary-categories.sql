# Write your MySQL query statement below
select "High Salary" as category, sum(income > 50000) as accounts_count
from Accounts

UNION

select "Low Salary" as category, sum(income < 20000) as accounts_count
from Accounts

UNION

select "Average Salary" as category, sum(income between 20000 and 50000) as accounts_count
from Accounts



