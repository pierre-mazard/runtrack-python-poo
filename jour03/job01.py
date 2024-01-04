# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 13:47:36 2024

@author: Mazard Pierre
"""

class Ville:
    def __init__(self, nom: str, nb_habitants: int):
        self.__nom = nom
        self.__nb_habitants = nb_habitants

    def get_nom(self) -> str:
        return self.__nom

    def get_nb_habitants(self) -> int:
        return self.__nb_habitants

    def set_nom(self, nom: str) -> None:
        self.__nom = nom

    def set_nb_habitants(self, nb_habitants: int) -> None:
        self.__nb_habitants = nb_habitants

class Personne:
    def __init__(self, nom: str, age: int, ville: Ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self) -> None:
        self.__ville.set_nb_habitants(self.__ville.get_nb_habitants() + 1)

    def get_nom(self) -> str:
        return self.__nom

    def get_age(self) -> int:
        return self.__age

    def get_ville(self) -> Ville:
        return self.__ville

    def set_nom(self, nom: str) -> None:
        self.__nom = nom

    def set_age(self, age: int) -> None:
        self.__age = age

    def set_ville(self, ville: Ville) -> None:
        self.__ville = ville

ville_paris = Ville("Paris", 1000000)
print(f"Nombre d'habitants de la ville de Paris: {ville_paris.get_nb_habitants()} habitants")

ville_marseille = Ville("Marseille", 861635)
print(f"Nombre d'habitants de la ville de Marseille: {ville_marseille.get_nb_habitants()} habitants")

john = Personne("John", 45, ville_paris)
john.ajouterPopulation()

myrtille = Personne("Myrtille", 4, ville_paris)
myrtille.ajouterPopulation()

chloe = Personne("Chloé", 18, ville_marseille)
chloe.ajouterPopulation()

print(f"Mise à jour de la population de la ville de Paris: {ville_paris.get_nb_habitants()} habitants")
print(f"Mise à jour de la population de la ville de Marseille: {ville_marseille.get_nb_habitants()} habitants")
