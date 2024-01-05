# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 14:49:24 2024

@author: Mazard Pierre
"""

import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
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
            if carte.valeur == 'As':
                as_present = True
            if carte.valeur in ['Valet', 'Dame', 'Roi']:
                valeur += 10
            else:
                valeur += int(carte.valeur)
        if as_present and valeur <= 11:
            valeur += 10
        return valeur

    def prendre_carte(self, main):
        main.append(self.paquet.pop())

    def croupier_joue(self, main):
        while self.valeur_main(main) < 17:
            self.prendre_carte(main)

    def determiner_gagnant(self, main_joueur, main_croupier):
        if self.valeur_main(main_joueur) > 21:
            return 'Croupier'
        elif self.valeur_main(main_croupier) > 21:
            return 'Joueur'
        elif self.valeur_main(main_joueur) > self.valeur_main(main_croupier):
            return 'Joueur'
        else:
            return 'Croupier'


jeu = Jeu()
jeu.melanger()
main_joueur, main_croupier = jeu.distribuer()
print('Main du joueur:')
for carte in main_joueur:
    print(carte)
print('Main du croupier:')
print(main_croupier[0])
print('Le joueur prend une carte supplémentaire:')
jeu.prendre_carte(main_joueur)
for carte in main_joueur:
    print(carte)
print('Le croupier joue:')
jeu.croupier_joue(main_croupier)
for carte in main_croupier:
    print(carte)
print('Le gagnant est:', jeu.determiner_gagnant(main_joueur, main_croupier))

