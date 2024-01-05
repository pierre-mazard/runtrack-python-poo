# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 14:49:24 2024

@author: Mazard Pierre
"""

import random

class Carte:
    def __init(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
   
class jeu:
    def __init__(self):
        self.paquet = []
        couleurs = ['Coeur', 'Pique', 'Carreau', 'Trèfle']
        valeurs = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']
        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))
    
    def melanger(self):
        random.shuffle(self.paquet)
        