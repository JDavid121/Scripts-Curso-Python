# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 20:22:36 2020

@author: David
"""
"""
Creación de tuplas
 
"""

floor_types = ['Parking', 'Shops', 'Food Court', 'Offices']
floor_numbers = range(-1,3)
#Una tupla puede crearse a partir de una lista ejemplo
a =[1,2,3,4,5] #Lista de números.
a_tupla = tuple (a)
print(a_tupla)
#Una lista puede crearse a partir de una tupla ejemplo:
a_tupla = (1,2,3,4,5)
b = list(a_tupla)
print(b)
#Creación de una Tupla
tuppla1 = [] 
for i in floor_types:
    tuppla1.append(i)
print (tuppla1)
tuppla2 = tuple(tuppla1)
print(tuppla2)
#zipped = list(...) 
#print(zipped)   