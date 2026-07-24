SELECT DISTINCT 
    t1.user_id,
    ROUND(
        IFNULL(
            COUNT(CASE WHEN t2.action = 'confirmed' THEN 1 END) OVER(PARTITION BY t1.user_id) 
            / 
            NULLIF(COUNT(t2.action) OVER(PARTITION BY t1.user_id), 0), 
        0), 
    2) AS confirmation_rate
FROM Signups t1 
LEFT JOIN Confirmations t2 ON t1.user_id = t2.user_id;
