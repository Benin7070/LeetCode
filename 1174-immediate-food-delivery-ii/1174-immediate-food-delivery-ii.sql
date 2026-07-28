with cte as(
select *, row_number() over(partition by customer_id order by order_date , customer_pref_delivery_date) as pp from Delivery
)

select round(count(case when order_date=customer_pref_delivery_date and pp=1 then 1 end)/count(case when pp=1 then 1 end)*100,2) as immediate_percentage from cte;