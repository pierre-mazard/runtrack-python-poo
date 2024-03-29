# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 11:53:52 2024

@author: Mazard Pierre
"""

class Personne:
    def __init__(self, age= 14):
        self.age = age
        
    def afficherAge(self):
        print(f"L'âge de la personne est de {self.age} ans.")
        
    def bonjour(self):
        print("Hello")
        
    def modifierAge(self, age):
        self.age = age
        
class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    
    def afficherAge(self):
        print(f"J'ai {self.age} ans.")

class Professeur:
    def __init__(self, matiereEnsegnee, age):
        self.__matiereEnsegnee = matiereEnsegnee
        self.age = age
    def enseigner(self):
        print("Le cours va commencer")
    
    def getMatiereEnseignee(self):
        return self.__matiereEnsegnee
    
personne = Personne()
eleve = Eleve()


eleve.modifierAge(15)
eleve.bonjour()
eleve.allerEnCours()

professeur = Professeur("Physique", 40)


print("Hello")
professeur.enseigner()