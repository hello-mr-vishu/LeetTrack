select user_id , concat(UPPER(substr(name,1,1)),lower(substr(name,2))) as name
From Users
order by user_id