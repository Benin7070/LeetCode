select name from SalesPerson s where sales_id not in (
select s.sales_id from Orders t1 join Company t2 on t1.com_id=t2.com_id where t2.name="RED" and t1.sales_id=s.sales_id);