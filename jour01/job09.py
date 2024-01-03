# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 14:25:42 2024

@author: Mazard Pierre
"""


class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)
    
    def afficher(self):
        print(f"Nom du produit : {self.nom}.")
        print(f"Prix HT : {self.prixHT}.")
        print(f"TVA : {self.TVA}%.")
        print(f"Prix TTC : {self.CalculerPrixTTC()}.")
        
    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom
        
    def modifierPrixHt(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT
    
    def getNom(self):
        return self.nom
    
    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA
    
produit1 = Produit("Livre broché", 15.50, 20)
produit2 = Produit("Crayon", 2, 15)

produit1.afficher()
produit2.afficher()

produit1.modifierNom("Livre non broché")
produit1.modifierPrixHt(12)

produit2.modifierNom("Stylo bic")
produit2.modifierPrixHt(3.50)

print("\n Après modifications : ")
produit1.afficher()
produit2.afficher()
