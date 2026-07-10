select Department,Employee,Salary from(select
        t2.name as Department,
        t1.name as Employee,
        t1.salary as Salary,
        dense_rank() over(partition by t1.departmentId order by t1.salary desc) as ranks
        from Employee t1 join department t2 on t1.departmentId=t2.id
)as tmp where tmp.ranks<=3;
    