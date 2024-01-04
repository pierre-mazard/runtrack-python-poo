# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:14:03 2024

@author: Mazard Pierre
"""

class Tache:
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, tache):
        self.taches.remove(tache)

    def marquerCommeFinie(self, tache):
        tache.statut = "terminée"

    def afficherListe(self):
        for tache in self.taches:
            print(f"{tache.titre} ({tache.statut}): {tache.description}")

    def filterListe(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]

tache1 = Tache("Faire les courses", "Acheter du lait, du pain et des oeufs", "à faire")
tache2 = Tache("Faire la lessive", "Laver les vêtements", "à faire")
tache3 = Tache("Appeler le médecin", "Prendre rendez-vous pour une consultation", "à faire")

listeDeTaches = ListeDeTaches()
listeDeTaches.ajouterTache(tache1)
listeDeTaches.ajouterTache(tache2)
listeDeTaches.ajouterTache(tache3)

listeDeTaches.afficherListe()

listeDeTaches.marquerCommeFinie(tache1)

listeDeTaches.afficherListe()

listeDeTaches.supprimerTache(tache2)

listeDeTaches.afficherListe()

tachesAFaire = listeDeTaches.filterListe("à faire")
print("Tâches à faire:")
for tache in tachesAFaire:
    print(f"{tache.titre}: {tache.description}")
