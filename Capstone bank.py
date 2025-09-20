from abc import ABC, abstractmethod 
class bank(ABC):
    def __init__(self,name,balance):
        self.__name = name 
        self.__balance = balance
    def get_name (self):
        return self.__name
    def get_balance (self):
        return self.__balance    
    def set_balance(self,amount):
        if amount >= 0 :
         self.__balance = amount
        else:
            print("Balance cannot be negative") 
    @abstractmethod
    def account_type(self):
        pass
class savingsaccount(bank):
    def account_type(self):
        return "Savings Account"    
       