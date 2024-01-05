# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 14:19:56 2024

@author: Mazard Pierre
"""

class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
        
    def informationVehicule(self):
        print(f"Marque : {self.marque}\nModèle : {self.modele}\nAnnée : {self.annee}\nPrix : {self.prix}")
        
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4 
        
    def informationVehicule(self):
        super().informationVehicule()
        print(f"Nombre de portes : {self.portes}")
        
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roue = 2
        
    def informationVehicule(self):
        super().informationVehicule()
        print(f"Nombre de roues : {self.roue}")
        
moto01 = Moto("Yamaha", "1200 Vmax", "1987", "4500")

moto01.informationVehicule()