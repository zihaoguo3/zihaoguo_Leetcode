# Write your MySQL query statement below
SELECT email as Email FROM(
SELECT COUNT(email) as counting, email FROM Person
GROUP BY email) as counting_email
WHERE counting>1


