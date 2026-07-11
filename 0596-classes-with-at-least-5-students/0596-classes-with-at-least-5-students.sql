select class from (
    select distinct class, count(student) over(partition by class)as students from Courses
) as tmp where students>=5;