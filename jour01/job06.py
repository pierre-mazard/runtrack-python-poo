# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 13:52:30 2024

@author: Mazard
"""

class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
        
    def vieillir(self):
        self.age +=1
    
    def nommer(self, prenom):
        self.prenom = prenom
        
animal = Animal()
print(f"L'âge de l'animal est {animal.age} ans.")
animal.vieillir()
print(f"L'âge de l'animal est maintenant de {animal.age} ans. ")
animal.nommer("Cannelle")
print(f"Le nom de l'animal est {animal.prenom}.")     
