# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 12:05:49 2024

@author: Mazard Pierre
"""

class Personne:
    def __init__(self, prenom, nom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"
    
personne1 = Personne("Pierre", "Mazard" )
personne2 = Personne("Antoine", "Durand")
personne3 = Personne("Juliette", "Jiuliani" )
personne4 = Personne("Bénédicte", "Brest")
personne5 = Personne("Damien", "Mouroux")

print(personne1.SePresenter())
print(personne2.SePresenter())
print(personne3.SePresenter())
print(personne4.SePresenter())
print(personne5.SePresenter())

