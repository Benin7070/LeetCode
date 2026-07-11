with data as (
    select tiv_2015,tiv_2016,count(tiv_2015) over( partition by(tiv_2015)) as rep,lat,lon from Insurance 
)

select round(cast(sum(tiv_2016) as float),2) as tiv_2016 from data where (lat,lon) in (
    select lat,lon from data group by lat,lon having count(*)=1
) and data.rep>1;