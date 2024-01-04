# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 13:30:31 2024

@author: Mazard Pierre
"""

class Commande:
    def __init__(self, num_commande: int, liste_plats: dict, statut: str):
        self.__num_commande = num_commande
        self.__liste_plats = liste_plats
        self.__statut = statut

    def ajouter_plat(self, nom_plat: str, prix: float, statut: str) -> None:
        self.__liste_plats[nom_plat] = {"prix": prix, "statut": statut}

    def annuler_commande(self) -> None:
        self.__statut = "annulée"

    def __calculer_total(self) -> float:
        total = 0
        for plat in self.__liste_plats.values():
            if plat["statut"] == "en cours":
                total += plat["prix"]
        return total

    def afficher_commande(self) -> str:
        total = self.__calculer_total()
        message = "Commande #" + str(self.__num_commande) + "\n"
        message += "Plats commandés:\n"
        for nom_plat, plat in self.__liste_plats.items():
            message += "- " + nom_plat + " (" + plat["statut"] + "): " + str(plat["prix"]) + "€\n"
        message += "Total à payer: " + str(total) + "€\n"
        return message

    def calculer_TVA(self, taux_TVA: float) -> float:
        total = self.__calculer_total()
        TVA = total * taux_TVA / 100
        return TVA

    def get_num_commande(self) -> int:
        return self.__num_commande

    def get_liste_plats(self) -> dict:
        return self.__liste_plats

    def get_statut(self) -> str:
        return self.__statut

    def set_num_commande(self, num_commande: int) -> None:
        self.__num_commande = num_commande

    def set_liste_plats(self, liste_plats: dict) -> None:
        self.__liste_plats = liste_plats

    def set_statut(self, statut: str) -> None:
        if statut not in ["en cours", "terminée", "annulée"]:
            raise ValueError("Le statut doit être 'en cours', 'terminée' ou 'annulée'")
        self.__statut = statut
