# Write your MySQL query statement below
select u.name ,sum(amount) AS balance
FROM Transactions t
inner join users u
on t.account = u.account
group by u.name
having sum(amount) > 10000