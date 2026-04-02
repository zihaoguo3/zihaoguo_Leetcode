# Write your MySQL query statement below
Select *, case when (x+y)>z and (y+z)>x and (x+z)>y then 'Yes' else 'No' end as triangle
from Triangle
