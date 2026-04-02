# Write your MySQL query statement below
with firstlogin as(
    select player_id, min(event_date) as first_date
    from Activity
    group by player_id
) 
select round(count(a.player_id)/(select count(distinct player_id) from Activity),2) as fraction
from Activity a 
join firstlogin f on f.player_id=a.player_id
where a.event_date=date_add(f.first_date,INTERVAL 1 day)
