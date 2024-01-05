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
    
    