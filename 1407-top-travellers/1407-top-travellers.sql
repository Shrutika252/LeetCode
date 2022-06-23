select Users.name, 
case
when sum(Rides.distance)>0
then sum(Rides.distance) else 0 end as travelled_distance 
from Users left join Rides on Users.id=Rides.user_id group by Users.id order by sum(Rides.distance) desc, Users.name;