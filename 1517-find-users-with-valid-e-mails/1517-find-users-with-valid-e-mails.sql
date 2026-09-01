# Write your MySQL query statement below
select * from Users where mail COLLATE utf8mb3_bin REGEXP '^[A-Za-z][A-Za-z0-9_\\.\\-]*@leetcode\\.com$';