Left join is the sql operation that helps to join two tables(one table primary key that added in the second table) and access the data from two tables.

Answer:
# Write your MySQL query statement below
select pt.firstname, pt.lastname, at.city, at.state from Person pt left join Address at on at.personId = pt.personId;
