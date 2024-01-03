# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 13:26:21 2024

@author: Mazard Pierre
"""

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def afficherLesPoints(self):
        print(f"Les coordonées du point sont ({self.x}, {self.y}).")
    
    def afficherX(self):
        print(f"La coordonnée horiozontale du point est {self.x}.")
        
    def afficherY(self):
        print(f"La coordonnnée verticale du point est {self.y}.")
        
    def changerX(self, x):
        self.x = x
    
    def changerY(self, y):
        self.y = y
    
point = Point(2, 6)
point.afficherLesPoints()
point.afficherX()
point.afficherY()
point.changerX(9)
point.changerY(7)
point.afficherLesPoints()


