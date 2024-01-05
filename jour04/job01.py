# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 10:59:56 2024

@author: Mazard Pierre
"""

class Personne:
    def __init__(self, age= 14):
        self.age = age
        
    def afficherAge(self):
        print(f"L'âge de la personne est de {self.age} ans.")
        
    def bonjour(self):
        print("Hello")
        
    def modifierAge(self, age):
        self.age = age
        