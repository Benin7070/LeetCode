select distinct Department , Employee, Salary from (
    select t2.name as Department, t1.name as Employee, t1.salary as Salary, max(t1.salary) over(partition by t1.departmentId) as max_Salary from Employee t1 join Department t2 on t1.departmentId=t2.id
)as tmp where Salary=tmp.max_Salary;