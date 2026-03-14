CREATE TABLE Salesman1(
Slm_id INT PRIMARY KEY,
Name VARCHAR(20),
City VARCHAR(10),
Comission INT
);
INSERT INTO Salesman1(Slm_id,Name,City,Comission)VALUES
(101,"Moni","BBSR",10),
(102,"Abhishek","Delhi",5),
(103,"Aashna","Raipur",7),
(104,"Divya","Jodhpur",12),
(105,"Shaan","Ranchi",4),
(106,"Raghav","Jaipur",20),
(107,"Padma","Cuttack",15);

SELECT * from Salesman1;

CREATE TABLE Customer1(
Cstmr_id INT PRIMARY KEY,
Cstmr_name VARCHAR(20),
Cstmr_city VARCHAR(10),
Grade TEXT,
Slm_id INT
);
INSERT INTO Customer1(Cstmr_id,Cstmr_name,Cstmr_city,Grade,Slm_id)VALUES
(201,"Mahi","BBSR","N",101),
(202,"Abhi","Delhi","D",102),
(203,"Ankita","Raipur","P",106),
(204,"Adwit","Jodhpur","P",106),
(205,"Riyaan","Ranchi","D",101),
(206,"Mehek","Jaipur","N",102),
(207,"Shlok","Cuttack","D",105);

SELECT * from Customer1;


CREATE TABLE Order1(
Ordr_no INT PRIMARY KEY,
Prchs_dt DATE,
Ordr_amt INT,
Cstmr_id TEXT,
Slm_id INT
);
INSERT INTO Order1(Ordr_no,Prchs_dt,Ordr_amt,Cstmr_id,Slm_id)VALUES
(112,"09-07-2024",40000,202,102),
(113,"11-08-2022",100000,201,101),
(114,"23-10-2023",89900,203,106),
(115,"06-11-2025",345000,202,102),
(116,"12-03-2021",250000,201,101),
(117,"31-03-2020",120000,203,106),
(118,"15-10-2025",500000,204,106);

SELECT * from Order1;

SELECT Customer1.Cstmr_name,Salesman1.Name,Salesman1.City
FROM Customer1
JOIN Salesman1 ON Customer1.Cstmr_city = Salesman1.City

SELECT Customer1.Cstmr_name,Salesman1.Name
FROM Customer1
JOIN Salesman1 ON Customer1.Slm_id = Salesman1.Slm_id

SELECT Order1.Ordr_no,Customer1.Cstmr_name, Order1.Cstmr_id,Order1.Slm_id
FROM Order1
JOIN Customer1 on Order1.Cstmr_id = Customer1.Cstmr_id
JOIN Salesman1 on Order1.Slm_id = Salesman1.Slm_id
WHERE Customer1.Cstmr_city != Salesman1.City;

SELECT Order1.Ordr_no,Customer1.Cstmr_name
FROM Order1
JOIN Customer1 on Order1.Cstmr_id = Customer1.Cstmr_id;

SELECT Customer1.Cstmr_name,Customer1.Grade
FROM Order1
JOIN Salesman1 on Order1.Slm_id = Salesman1.Slm_id
JOIN Customer1 on Order1.Cstmr_id = Customer1.Cstmr_id
WHERE Customer1.Grade IS NOT NULL;