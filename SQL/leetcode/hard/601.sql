WITH TEMP AS (
select
T101.id
, ifnull(lag (T101.people, 2) over (order by T101.visit_date asc), 0) as prev_prev_people
, ifnull(lag (T101.people, 1) over (order by T101.visit_date asc), 0) as prev_people
, T101.people
, T101.visit_date
, ifnull(lead (T101.people, 1) over (order by T101.visit_date asc), 0) as next_people
, ifnull(lead (T101.people, 2) over (order by T101.visit_date asc), 0) as next_next_people
from
Stadium T101
)
select 
T102.id
, T102.visit_date
, T102.people
from
    (
    select
    id
    , visit_date
    , people
    from TEMP
    where prev_prev_people >= 100 and prev_people >= 100 and people >= 100
    union
    select
    id
    , visit_date
    , people
    from TEMP
    where prev_people >= 100 and people >= 100 and next_people >= 100
    union
    select
    id
    , visit_date
    , people
    FROM TEMP
    where people >= 100 and next_people >= 100 and next_next_people >= 100
) T102
order by T102.visit_date asc
