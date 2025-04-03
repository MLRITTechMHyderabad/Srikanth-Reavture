# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 10:44:17 2025

@author: 91766
"""
class vehicle:
    def __init__(self,brand):
        self.brand=brand
    def v_display(self):
        print("veh:",self.brand)

class car(vehicle):
    def __init__(self,model,brand):
        super().__init__(brand)
        self.model=model
    def c_display(self):
        print(self.brand,self.model)
        
car=car("BMW","x")
car.v_display()
car.c_display()