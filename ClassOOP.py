class Plants:
    species = "flora"
    def __init__(self,name,soil_type,water):
        self.name = name
        self.soil = soil_type
        self.water = water 
    def details(self):
        print(f"Name : {self.name} \n Soil : {self.soil} \n Water : {self.water}mL")    

a = input("Enter the plant name : ")    
b = input("Enter the Soil Type : ")    
c = input("Enter the Water requirement : ")

plant1 = Plants(a,b,c)
plant1.details()

plant2 = Plants("Rose","Black soil","100")
plant2.details()
