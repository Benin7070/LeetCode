with data as (
    select distinct managerId, count(*) over(partition by managerId) as total from Employee
)

select name from Employee where id in(
    select managerId from data where total>=5
);