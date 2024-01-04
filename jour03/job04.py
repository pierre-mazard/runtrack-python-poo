# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:23:33 2024

@author: Mazard Pierre
"""

class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Nom: {self.nom}")
        print(f"Numéro: {self.numero}")
        print(f"Position: {self.position}")
        print(f"Buts marqués: {self.buts_marques}")
        print(f"Passes décisives effectuées: {self.passes_decisives}")
        print(f"Cartons jaunes reçus: {self.cartons_jaunes}")
        print(f"Cartons rouges reçus: {self.cartons_rouges}")

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []

    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)

    def AfficherStatistiquesJoueurs(self):
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom, buts_marques, passes_decisives, cartons_jaunes, cartons_rouges):
        for joueur in self.liste_joueurs:
            if joueur.nom == nom:
                joueur.buts_marques += buts_marques
                joueur.passes_decisives += passes_decisives
                joueur.cartons_jaunes += cartons_jaunes
                joueur.cartons_rouges += cartons_rouges


joueur1 = Joueur("Jean", 10, "Attaquant")
joueur2 = Joueur("Pierre", 5, "Milieu de terrain")
joueur3 = Joueur("Paul", 1, "Gardien de but")


equipe1 = Equipe("Equipe 1")
equipe2 = Equipe("Equipe 2")


equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)


print("Statistiques des joueurs avant le match:")
equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()


joueur1.marquerUnBut()
joueur1.effectuerUnePasseDecisive()
joueur2.recevoirUnCartonJaune()
joueur3.recevoirUnCartonRouge()

equipe1.mettreAJourStatistiquesJoueur("Jean", 1, 1, 0, 0)
equipe1.mettreAJourStatistiquesJoueur("Pierre", 0, 0, 1, 0)
equipe2.mettreAJourStatistiquesJoueur("Paul", 0, 0, 0, 1)


print("Statistiques des joueurs après le match:")
equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()
