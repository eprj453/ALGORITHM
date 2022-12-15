SELECT
T301.Department
, T301.Employee
, T301.Salary
FROM
(
    SELECT
    T201.Department
    , T201.Employee
    , DENSE_RANK () OVER (partition by T201.Department order by T201.Salary desc) AS 'salary_rank'
    , T201.Salary
    FROM
        (
            SELECT
            T101.name as 'Employee'
            , T101.salary as 'Salary'
            , T102.name as 'Department'
            FROM Employee T101
            INNER JOIN Department T102
            ON T101.departmentId = T102.id
        ) T201
) T301
WHERE T301.salary_rank <= 3