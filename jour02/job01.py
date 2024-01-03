# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 14:42:13 2024

@author: Mazard . Pierre
"""

#                       Définition de la classe
class Rectangle:
    def __init__(self, longueur, largeur):
#                       Initialisation des attributs privés
        self.__longueur = longueur
        self.__largeur = largeur

#                       Assersseur pour l'attribut longueur
    def get_longueur(self):
        return self.__longueur

#                       Mutateur pour l'attribut longueur
    def set_longueur(self, longueur):
        self.__longueur = longueur
        
#                       Assersseur pour l'attribut largeur
    def get_largeur(self):
        return self.__largeur

#                       Mutateur pour l'attribut largeur
    def set_largeur(self, largeur):
        self.__largeur = largeur
    
#                       Création d'un objet rectangle aves les valeurs longeur = 10 et largeur = 5
rectangle = Rectangle(10, 5)

#                       Modification de la valeur de la longueur et de la largeur
rectangle.set_longueur(28)
rectangle.set_largeur(19)

#                       Affichage des nouvelles valeurs de longueur et de largeur à l'aide des assersseurs
print(f"La longueur du rectangle est de {rectangle.get_longueur()} et la largeur de {rectangle.get_largeur()}.")

