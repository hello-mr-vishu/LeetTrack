with cte AS 
(SELECT *
FROM Students
CROSS JOIN Subjects),
cte2 AS 
(SELECT student_id,subject_name , COUNT(subject_name)
AS count
FROM Examinations 
group by student_id , subject_name)

select cte.student_id , cte.student_name , 
cte.subject_name ,case when count is not null then 
count else 0 end as attended_exams
FROM cte 
LEFT Join cte2
on cte.student_id = cte2.student_id
and cte.subject_name = cte2.subject_name 
order by cte.student_id, cte.subject_name   