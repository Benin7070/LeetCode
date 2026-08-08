with cte as(
    select 'Low Salary' as category union all
    select 'Average Salary' union all
    select 'High Salary'
)

select t1.category, count(t2.account_id) as accounts_count from cte t1 left join Accounts t2 
ON (t1.category = 'Low Salary' AND t2.income < 20000)
  OR (t1.category = 'Average Salary' AND t2.income BETWEEN 20000 AND 50000)
  OR (t1.category = 'High Salary' AND t2.income > 50000) 
group by t1.category order by accounts_count desc;