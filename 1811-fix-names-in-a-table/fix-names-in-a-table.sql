# Write your MySQL query statement below
SELECT user_id,
    CONCAT(
        UPPER(SUBSTRING(name, 1, 1)), -- Convert first character to uppercase
        LOWER(SUBSTRING(name, 2))    -- Convert remaining characters to lowercase
    ) AS name
FROM users
order by user_id;