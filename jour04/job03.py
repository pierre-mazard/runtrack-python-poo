# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:04:54 2024

@author: Mazard Pierre
"""

class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur 
        
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
        
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
        
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
        
    def volume(self):
        return self.__longueur * self.__largeur * self.__hauteur
    
    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur
        
rectangle01 = Rectangle(13, 21)

print(f"Le périmètre du rectangle est de : {rectangle01.perimetre()} .")
print(f"La surface du rectangle est de : {rectangle01.surface()} .")
       