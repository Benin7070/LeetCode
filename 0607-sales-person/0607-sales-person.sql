select name from SalesPerson where sales_id not in (
select t3.sales_id from Orders t1 join Company t2 on t1.com_id=t2.com_id join SalesPerson t3 on t1.sales_id=t3.sales_id where t2.name="RED" );