# Write your MySQL query statement below
SELECT teacher_id , 
count(DISTINCT subject_id) as  cnt
From Teacher
group by teacher_id