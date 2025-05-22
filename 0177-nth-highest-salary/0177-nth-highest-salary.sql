CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    with cte as
    (select *,DENSE_RANK() over(order by salary desc) as rnk
      from employee)

    select distinct ifnull(salary ,null)
    from cte 
    where rnk = N

  );
END