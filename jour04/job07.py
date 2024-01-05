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
    
    def distribuer(self):
        main_joueur = []
        main_croupier = []
        for i in range(2):
            main_joueur.append(self.paquet.pop())
            main_croupier.append(self.paquet.pop())
        return main_joueur, main_croupier
    
    def valeur_main(self, main):
        valeur = 0
        as_present = False
        for carte in main:
            if carte.valeur == "As":
                as_present = True
            if carte.valeur in ['Valet', 'Dame', 'Roi']:
                valeur += 10
            else:
                valeur += int(carte.valeur)
        if as_present and valeur <= 11:
            valeur += 10
        return valeur