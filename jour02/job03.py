# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:56:39 2024

@author: Mazard Pierre
"""

class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages
        self.__disponible = True
    
    def get_titre(self):
        return self.__titre
    
    def set_titre(self, titre):
        self.__titre = titre
        
    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, auteur):
        self.__auteur = auteur
        
    def get_nombre_de_pages(self):
        return self.__nombre_de_pages
    
    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print("Le nombre de pages doit être un nombre entier positif.")
    
    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre a été emprunté avec succès.")
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")
    
    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre a été rendu avec succès.")
        else:
            print("Le livre n'a pas été emprunté.")
            
livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 100)

livre.set_nombre_de_pages(200)

print(f"Le livre \"{livre.get_titre()}\" écrit par {livre.get_auteur()} a {livre.get_nombre_de_pages()} pages.")
livre.emprunter()
print(f"Le livre est disponible : {livre.verification()}")
livre.rendre()
print(f"Le livre est disponible : {livre.verification()}")
