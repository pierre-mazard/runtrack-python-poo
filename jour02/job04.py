# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 11:08:54 2024

@author: Mazard Pierre
"""

class Student: 
    def __init__(self, first_name, last_name, student_id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_id = student_id
        self.__credits = 0
        
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
        else:
            print("Lenombre de crédits doit être supérieur à zéro.")
    
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_credits(self):
        return self.__credits
         
student01 = Student("John", "Doe", 145)

student01.add_credits(15)
student01.add_credits(3)
student01.add_credits(26)

print(f"Le total des crédits obtenus par {student01.get_first_name()} {student01.get_last_name()} est de {student01.get_credits()}")
       