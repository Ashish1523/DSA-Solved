# Write your MySQL query statement below
select name from salesperson where name not in
(select s.name from salesperson s join company c join orders o where c.com_id=o.com_id and o.sales_id=s.sales_id and c.name="red")