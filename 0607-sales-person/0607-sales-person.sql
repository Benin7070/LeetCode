select name from SalesPerson where name not in (
select t3.name from Orders t1 left join Company t2 on t1.com_id=t2.com_id join SalesPerson t3 on t1.sales_id=t3.sales_id where t2.name="RED" );