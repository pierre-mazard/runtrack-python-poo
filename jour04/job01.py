# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 10:59:56 2024

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
    def __init__(self, matiereEnsegnee):
        self.__matiereEnsegnee = matiereEnsegnee
    
    def enseigner(self):
        print("Le cours va commencer")
    
    def getMatiereEnseignee(self):
        return self.__matiereEnsegnee
    
personne = Personne()
eleve = Eleve()

print (f"L'âge par défaut de l'élève est de {eleve.age} ans.")