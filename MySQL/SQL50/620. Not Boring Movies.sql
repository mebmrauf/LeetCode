-- 620. Not Boring Movies
-- https://leetcode.com/problems/not-boring-movies/?envType=study-plan-v2&envId=top-sql-50

SELECT Cinema.id, Cinema.movie, Cinema.description, Cinema.rating
FROM Cinema
WHERE Cinema.id % 2 = 1 AND Cinema.description != 'boring'
ORDER BY Cinema.rating DESC;