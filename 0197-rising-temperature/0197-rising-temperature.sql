select id from(
    select id,temperature, recordDate,lag(temperature) over(order by recordDate) as bef_temp ,
    lag(recordDate) over(order by recordDate) as bef_day,
    DATE_SUB(recordDate, INTERVAL 1 DAY) AS yesterday from Weather
) as tmp where tmp.temperature>tmp.bef_temp and tmp.bef_day=tmp.yesterday;