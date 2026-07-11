with data as(
    select distinct customer_number,count(order_number) over(partition by customer_number) as orders from Orders
)
select customer_number from data where orders=(select max(orders) from data);