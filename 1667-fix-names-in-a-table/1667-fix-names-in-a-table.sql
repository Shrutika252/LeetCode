Select user_id , concat((UPPER(left(name,1))),(LOWER(right(name, length(name)-1)))) as name
From Users
order by user_id
