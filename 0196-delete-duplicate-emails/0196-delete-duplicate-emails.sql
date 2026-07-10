
delete from person 
    where id in(
        select id from (
            select id,  row_number() over(partition by email order by id asc) as num from Person 
        )as tmp where tmp.num>1
    );