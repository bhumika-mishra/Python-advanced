CREATE TABLE Student(
Rollno TEXT PRIMARY KEY ,
Name TEXT NOT NULL,
Address TEXT,
Phone TEXT,
Age INTEGER
);

INSERT INTO Student(Rollno,Name,Address,Phone,Age) VALUES
('1','Arpita','Nagpur','9768546783','17'),
('2','Arya','Delhi','8907634512','16'),
('3','Ram','Cuttack','9786434578','18'),
('4','Divya','Mohali','7896547658','20'),
('5','Aarav','Delhi','8900123401','18'),
('6','Sujit','Jaipur','9437698051','15');

SELECT * from Student
WHERE Age='18' AND Address='Delhi';

SELECT * from Student
WHERE Name='Ram' AND Age='18';

SELECT * from Student
WHERE Name='Ram' OR Name='Sujit';

SELECT * from Student
WHERE Name='Ram' OR Age='20';

SELECT * from Student
WHERE  Age='18' AND (Name='Ram' OR Name='Ramesh');



CREATE TABLE Product(
Prod_id TEXT PRIMARY KEY ,
Prod_name TEXT,
Prod_price TEXT,
Prod_com TEXT
);

INSERT INTO Product(Prod_id,Prod_name,Prod_price,Prod_com)VALUES
('101','Printer','25000','10'),
('102','TV','80000','10'),
('103','Laptop','75000','10'),
('104','Keyboard','3000','10'),
('105','Hard disk','9000','10'),
('106','Mouse','500','10');

SELECT Prod_name,MAX(Prod_price) from Product;

SELECT MIN(Prod_price) AS CHEAPESTPRICE from Product;

