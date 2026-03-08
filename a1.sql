CREATE TABLE Department1(
Eid TEXT,
Name TEXT,
Dept_id TEXT,
Mngr_id TEXT,
Salary INT
);

INSERT INTO Department1(Eid,Name,Dept_id,Mngr_id,Salary)VALUES
("501","Aarya","Sales","109",30000),
("502","Prachi","IT","107",80000),
("503","Devesh","IT","107",65000),
("504","Arpita","Finance","101",100000),
("505","Divya","Marketing","100",50000),
("506","Saina","IT","107",130000),
("507","Abhishek","Marketing","100",35000);

SELECT Dept_id,COUNT(*) from Department GROUP BY Dept_id;

SELECT Dept_id, SUM(Salary) from Department GROUP BY Dept_id;

SELECT Dept_id, COUNT(*) ,SUM(Salary) from Department GROUP BY Dept_id;

SELECT Dept_id, COUNT(*) ,SUM(Salary) 
from Department 
WHERE Mngr_id="107"
GROUP BY Dept_id;

SELECT Dept_id,Count(*) from Department1 
GROUP BY Dept_id
HAVING COUNT(*)>2;