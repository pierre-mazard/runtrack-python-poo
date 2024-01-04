# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 14:07:08 2024

@author: Mazard Pierre
"""

class CompteBancaire:
    def __init__(self, numero_compte: str, nom: str, prenom: str, solde: float, decouvert: bool):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Numéro de compte: {self.__numero_compte}\nNom: {self.__nom}\nPrénom: {self.__prenom}\nSolde: {self.__solde}\nDécouvert autorisé: {self.__decouvert}")

    def afficherSolde(self):
        print(f"Le solde du client est de {self.__solde} euros.")

    def versement(self, montant: float):
        self.__solde += montant
        print(f"Le versement de {montant} euros a été effectué avec succès. Le nouveau solde est de {self.__solde} euros.")

    def retrait(self, montant: float):
        if self.__decouvert or montant <= self.__solde:
            self.__solde -= montant
            print(f"Le retrait de {montant} euros a été effectué avec succès. Le nouveau solde est de {self.__solde} euros.")
        else:
            print("Le montant à retirer est supérieur au solde disponible et au découvert autorisé.")



compte = CompteBancaire("145698741", "Mazard", "Pierre", 1500.66, True)

compte.afficher()
compte.afficherSolde()
compte.versement(536.23)
compte.retrait(240.0)
compte.retrait(4000.0)