# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 14:11:05 2024

@author: Mazard Pierre
"""

class Forme:
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur
    
    def aire(self):
        return self.__largeur * self.__hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.__radius = radius
        
    def aire(self):
        return 3.14 * self.__radius ** 2
    
rectangle01 = Rectangle(6, 12)
cercle01 = Cercle(4.5)

print (f"L'aire du rectangle est de : {rectangle01.aire()} . \n L'aire du cercle est de : {cercle01.aire()} .")
        