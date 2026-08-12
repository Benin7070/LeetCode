with cte2 as (
select visited_on,sum(amount) as amount from Customer group by visited_on
)
,

cte as(
select visited_on, SUM(amount) OVER (
        ORDER BY visited_on 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS amount,
    ROUND(
        AVG(amount) OVER (
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ), 2) as average_amount,
    row_number() over(order by visited_on) as days from cte2
)


select visited_on, amount, average_amount from cte where days>=7;