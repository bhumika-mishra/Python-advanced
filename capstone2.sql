CREATE TABLE Restaurant(
Name VARCHAR(20),
Neighborhood VARCHAR(10),
Cuisine VARCHAR(20),
Price VARCHAR(4),
Health TEXT
);

INSERT INTO Restaurant(Name,Neighborhood,Cuisine,Price,Health)VALUES 
("Spicy Flames","Surya Vihar","South Indian","500","4.5"),
("Jimizz Restaurant","CDA Sector-9","Italian","800","4.3"),
("Aromas","Link Rd","South Indian","600","4.8"),
("Wedesi","Link Rd","Chinese","1000","4.8"),
("Delly Belly","Surya Vihar","Italian","800","4.5"),
("Sunday Cafe","CDA Sector-9","Italian","600","4.8"),
("Blast Restaurant","CDA Sector-9","Chinese","700","4.2"),
("Restro Cafe","Surya Vihar","Italian","800","4.7");

SELECT DISTINCT Neighborhood from Restaurant;

SELECT Name from Restaurant WHERE Health >= "4";

SELECT Name from Restaurant WHERE Cuisine = "Italian";

SELECT Name from Restaurant WHERE Name LIKE "S%";

SELECT Name,Health AS Rating from Restaurant 
ORDER BY Health DESC 
LIMIT 4;