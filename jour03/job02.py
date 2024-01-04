# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 14:07:08 2024

@author: Mazard Pierre
"""

class CompteBancaire:
    def __init__(self, numero_compte: str, nom: str, prenom: str, solde: float, decouvert: bool = False):
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

    def agios(self, taux: float):
        if self.__solde < 0:
            agios = abs(self.__solde) * taux
            self.__solde -= agios
            print(f"Des agios de {agios} euros ont été appliqués. Le nouveau solde est de {self.__solde} euros.")
        else:
            print("Le solde du compte est positif. Aucun agio n'a été appliqué.")

    def virement(self, reference: str, compte_destinataire, montant: float):
        if montant > self.__solde:
            print("Le montant à transférer est supérieur au solde disponible.")
        else:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Le virement de {montant} euros vers le compte {reference} a été effectué avec succès. Le nouveau solde est de {self.__solde} euros.")


compte1 = CompteBancaire("123456789", "Dupont", "Jean", 1000.0)


compte2 = CompteBancaire("987654321", "Durand", "Marie", -500.0, True)


compte1.afficher()
compte2.afficher()

compte1.virement("987654321", compte2, 500.0)


compte1.afficher()
compte2.afficher()


