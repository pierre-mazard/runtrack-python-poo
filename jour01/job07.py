# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 14:04:32 2024

@author: Mazard Pierre
"""

class Personnage:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def gauche(self):
        self.x -=1
        
    def droite(self):
        self.x +=1
        
    def haut(self):
        self.y -=1
        
    def bas(self):
        self.y +=1
    
    def position(self):
        return (self.x, self.y)

personnage = Personnage(8, 6)
print(f"La position du personnage est {personnage.position()}.")
personnage.gauche()
print(f"La position du personnage est {personnage.position()}.")
personnage.droite()
print(f"La position du personnage est {personnage.position()}.")
personnage.haut()
print(f"La position du personnage est {personnage.position()}.")
personnage.bas()
print(f"La position du personnage est {personnage.position()}.")