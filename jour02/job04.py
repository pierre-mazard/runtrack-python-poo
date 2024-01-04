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
        self.__level = self.__studentEval()
        
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__studentEval()
        else:
            print("Lenombre de crédits doit être supérieur à zéro.")
    
    def __studentEval(self):
        if self.__credits >=90:
            return "Excellent"
        elif self.__credits >=80:
            return "Très bien"
        elif self.__credits >=70:
            return "Bien"
        elif self.__credits >=60:
            return "Passable"
        else:
            return "Insuffisant"
        
    def studentInfo(self):
        print(f"Nom: = {self.__last_name}")
        print(f"Prénom = {self.__first_name}")
        print(f"id = {self.__student_id}")
        print(f"Niveau = {self.__level}")
         
student01 = Student("John", "Doe", 145)

student01.add_credits(15)
student01.add_credits(3)
student01.add_credits(26)

student01.studentInfo()
       