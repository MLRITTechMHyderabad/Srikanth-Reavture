# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 09:06:49 2025

@author: 91766
"""

from abc import ABC,abstractmethod
class Chai(ABC):
    def __init__(self,name,base_price,quantity_in_stock):
        self.name=name
        self.base_price=base_price
        self.quantity_in_stock=quantity_in_stock

    @abstractmethod
    def calculate_price(self):
        pass
    def display_info(self):
        pass
        # print(f"Chai Name: {self.name}")
        # print(f"Base Price: {self.base_price}")
        # print(f"Quantity in Stock: {self.quantity_in_stock}")

class Masalachai(Chai):
    def __init__(self, name, base_price, quantity_in_stock):
        super().__init__(name, base_price, quantity_in_stock)
        self.spice_level = 10  

    def calculate_price(self):
       
        return self.base_price + self.spice_level #* 2

    def display_info(self):
        super().display_info()
        print(f"Name: {self.name} | Price per cup: ₹{self.calculate_price()} | Stock: {self.quantity_in_stock}")
        # print(f"Spice Level: {self.spice_level}")
        # print(f"Total Price: {self.calculate_price()}")
    

class Gingerchai(Chai):
    def __init__(self,name, base_price, quantity_in_stock):
        super().__init__(name, base_price, quantity_in_stock)
        self.spice_level = 8
    
    def calculate_price(self):
        return self.base_price + self.spice_level# * 2

    def display_info(self):
        super().display_info()
        # print(f"Spice Level: {self.spice_level}")
        print(f"Name: {self.name} | Price per cup: ₹{self.calculate_price()} | Stock: {self.quantity_in_stock}")
        # print(f"Total Price: {self.calculate_price()}")

class Elachchai(Chai):
    def __init__(self,name, base_price, quantity_in_stock):
        super().__init__(name, base_price, quantity_in_stock)
        self.spice_level = 12
    def calculate_price(self):
        return self.base_price + self.spice_level # * 2
    def display_info(self):
        super().display_info()
        # print(f"Spice Level: {self.spice_level}")
        print(f"Name: {self.name} | Price per cup: ₹{self.calculate_price()} | Stock: {self.quantity_in_stock}")
        # print(f"Total Price: {self.calculate_price()}")

class ChaiInventory(Chai):
    def __init__(self,chai_type,quantity_in_stock):
        self.chai_type=chai_type
        self.quantity_in_stock=quantity_in_stock
        self.inventory=[]
    def calculate_price(self):
        if self.chai_type=='Masala Chai':
            return 10*self.quantity_in_stock
        elif self.chai_type=='Ginger Chai':
            return 8*self.quantity_in_stock
        elif self.chai_type=='Elachi Chai':
            return 12*self.quantity_in_stock
        else:
            return 0
    def add_chai(self, chai):
        
        self.inventory.append(chai)
        self.quantity_in_stock+=chai.quantity_in_stock
        
    def get_total_inventory_value(self):    
        total_value = 0
        for chai in self.inventory:
            total_value += chai.calculate_price() * chai.quantity_in_stock
        return total_value
    def show_inventory(self):
        for chai in self.inventory:
            chai.display_info()
        #print(f"Chai Type: {self.chai_type}, Quantity in Stock: {self.quantity_in_stock}, Total Price: {self.calculate_price()}")
       
       #print(f"Chai Type: {self.chai_type}, Quantity in Stock: {self.quantity_in_stock}, Total Price: {self.calculate_price()}")

inventory = ChaiInventory("Masala Chai", 10)
chai1 = Masalachai("Masala Chai", 20, 50)
chai2 = Gingerchai("Ginger Chai", 18, 40)
chai3 = Elachchai("Elachi Chai", 25, 30)

inventory.add_chai(chai1)
inventory.add_chai(chai2)
inventory.add_chai(chai3)

inventory.show_inventory()

print("Total Inventory Value: ₹", inventory.get_total_inventory_value())