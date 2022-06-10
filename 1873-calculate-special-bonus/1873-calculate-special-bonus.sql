select employee_id,
CASE
    WHEN employee_id % 2 = 1 and name NOT LIKE 'M%' then salary
    ELSE 0
END AS bonus
from Employees
order by employee_id