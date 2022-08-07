with temp as(select count(*) as counts from Seat)
select case when mod(id,2)=1 and id!=counts then id+1
            when mod(id,2)=1 and id=counts then id
            when mod(id,2)=0 and id!=counts then id-1
            when mod(id,2)=0 and id=counts then id-1
            
            end as 'id',
            student from Seat,temp
            order by id

