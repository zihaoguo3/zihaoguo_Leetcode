# Write your MySQL query statement below
WITH ranking_table as(SELECT player_id, event_date, RANK() OVER(PARTITION BY player_id ORDER BY event_date ASC) as ranking FROM Activity)
SELECT player_id, event_date as first_login
FROM ranking_table
WHERE ranking=1
