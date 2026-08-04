select person_name from (
    select person_name, sum(weight) over(order by turn) as sum_weight from Queue
 ) as t where sum_weight<=1000 order by sum_weight desc limit 1;