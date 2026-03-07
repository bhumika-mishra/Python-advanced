CREATE TABLE Grocery(
Gid TEXT,
Gname TEXT,
Suplr_id TEXT,
Category_id TEXT,
Price INT,
Unit INT
);

INSERT INTO Grocery(Gid,Gname,Suplr_id,Category_id,Price,Unit)VALUES
("111","Sugar","5678","Beverage",45,1),
("112","Flour","8890","Daily needs",243,5),
("113","Oil","6364","Garnish",149,1),
("114","Sauce","7880","Beverage",90,1),
("115","Spices","7099","Garnish",100,10),
("116","Rice","8800","Daily needs",265,2),
("117","Face cream","7790","Toiletries",345,1);

SELECT SUM(Price*Unit)from Grocery;

SELECT Gname,MAX(Unit) from Grocery;

SELECT AVG(Price) from Grocery;

SELECT DISTINCT Category_id from Grocery;
