-- 1729. Find Followers Count
-- https://leetcode.com/problems/find-followers-count/?envType=study-plan-v2&envId=top-sql-50

SELECT Followers.user_id, COUNT(Followers.follower_id) AS followers_count
FROM Followers
GROUP BY Followers.user_id
ORDER BY Followers.user_id ASC;