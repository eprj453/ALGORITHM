SELECT
T201.user_id AS buyer_id
, T201.join_date
, IFNULL(T202.orders_in_2019, 0) AS orders_in_2019
FROM Users T201
LEFT JOIN (
    SELECT
    T101.buyer_id
    , COUNT(T101.item_id) AS orders_in_2019
    FROM Orders T101
    WHERE DATE_FORMAT(T101.order_date, '%Y') = '2019'
    GROUP BY T101.buyer_id
) T202
ON T201.user_id = T202.buyer_id
 
-- beat 47.95