from abc import ABC, abstractmethod
class Plant(ABC):
    kingdom = "Plantae"

    def __init__(self,name,height):
        self.__name = name
        self._height = height
    def get_name(self):
        return self.__name
    def set_name(self,newname):
       self.__name = newname
    @abstractmethod
    def grow(self):
        pass
    def details(self):
        return f"{self.__name} is {self._height}cm tall."   

class Flowering(Plant):
    def __init__(self,name,height,colour):
        super().__init__(name,height)
        self.colour = colour
    def grow(self):
        return  f"{self.get_name()} grow by producing {self.colour} colour flowers."

class NonFlowering(Plant):
    def __init__(self,name,height,spore_type):
        super().__init__(name,height)
        self.spore_type = spore_type
    def grow(self):
        return  f"{self.get_name()} grow by producing {self.spore_type} spores."    
if __name__ == "__main__":
    sunflower =  Flowering("Sunflower","180","Yellow")    
    print("Kingdom : ",Plant.kingdom)
    print(sunflower.details())
    print(sunflower.grow())
    print("\n")
    Fern =  NonFlowering("Fern","70","Tiny")    
    print("Kingdom : ",Plant.kingdom)
    print(Fern.details())
    print(Fern.grow())
     