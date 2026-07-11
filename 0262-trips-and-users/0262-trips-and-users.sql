with data as(
    select t.client_id,t.driver_id,t.status,t.request_at,u.banned as banned_user,s.banned as banned_driver from Trips t left join Users u on t.client_id = u.users_id left join Users s on t.driver_id=s.users_id
)

select tmp.Day as Day, Round((tmp.banned_req/tmp.unbanned_request),2) as 'Cancellation Rate' from
(
    select request_at as Day , count(CASE
        WHEN banned_user = 'No'
        AND banned_driver = 'No'
        AND status IN ('cancelled_by_client', 'cancelled_by_driver')
        THEN 1
        END) as banned_req, count(
            Case when banned_user="No" 
            and banned_driver="No" THEN 1 
            END) as unbanned_request from data 
            WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
            group by request_at having unbanned_request>0) as tmp;
