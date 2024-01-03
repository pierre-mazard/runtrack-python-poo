# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 14:12:00 2024

@author: Mazard Pierre
"""


class Cercle:
    def __init__(self, rayon):
        self.rayon= rayon
    
    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon
        
    def circonférence(self):
        return 2 * 3.14 * self.rayon
    
    def aire(self):
        return 3.14 * self.rayon ** 2
    
    def diametre(self):
        return 2 * self.rayon
    
    def afficherInfos(self):
        print(f"Rayon du cercle = {self.rayon}.")
        print(f"Circonférence du cercle = {self.circonférence()}.")
        print(f"Aire du cercle = {self.aire()}.")
        print(f"Diamètre du cercle = {self.diametre()}.")
    
cercle1 = Cercle(4)
cercle2 = Cercle(7)

print ("Cercle 1 :")
cercle1.afficherInfos()
print("\nCercle 2 :")
cercle2.afficherInfos()
