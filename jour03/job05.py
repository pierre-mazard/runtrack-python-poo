# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:28:41 2024

@author: Mazard Pierre
"""

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        adversaire.vie -= 10

class Jeu:
    def __init__(self):
        self.niveau = None

    def choisirNiveau(self):
        self.niveau = input("Choisissez le niveau de difficulté (facile, moyen, difficile): ")

    def lancerJeu(self):
        if self.niveau == "facile":
            joueur = Personnage("Joueur", 100)
            ennemi = Personnage("Ennemi", 50)
        elif self.niveau == "moyen":
            joueur = Personnage("Joueur", 75)
            ennemi = Personnage("Ennemi", 75)
        elif self.niveau == "difficile":
            joueur = Personnage("Joueur", 50)
            ennemi = Personnage("Ennemi", 100)

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            ennemi.attaquer(joueur)

        if joueur.vie > 0:
            print(f"{joueur.nom} a gagné!")
        else:
            print(f"{ennemi.nom} a gagné!")

# Création d'une instance de la classe Jeu
jeu = Jeu()

# Choix du niveau de difficulté
jeu.choisirNiveau()

# Lancement du jeu
jeu.lancerJeu()
