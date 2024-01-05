# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 14:03:44 2024

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


rectangle01 = Rectangle(23, 36)

print (f"L'aire du rectangle est de : {rectangle01.aire()} .")