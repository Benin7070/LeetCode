select distinct sub.num as ConsecutiveNums from (
    select id,num, Lead(num,1) over(order by id) as next_num, lead(num,2) over (order by id) as next_next_num from Logs
) sub  where sub.num=sub.next_num and sub.num=sub.next_next_num;