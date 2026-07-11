select round(( count(case when datediff(tmp.event_date,tmp.first_logged)=1 then 1 end)/
        count(distinct tmp.player_id)),2) as fraction from(    
    select player_id, event_date,
    min(event_date) over(partition by player_id) as first_logged 
    from Activity
) as  tmp;