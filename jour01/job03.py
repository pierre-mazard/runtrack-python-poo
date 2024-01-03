# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 12:01:16 2024

@author: Mazard Pierre
"""

class Operation:
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    
    def addition(self):
        result = self.nombre1 + self.nombre2
        print(f"La somme de {self.nombre1} et {self.nombre2} est égale à {result}")
    
operation = Operation()
operation.addition()
