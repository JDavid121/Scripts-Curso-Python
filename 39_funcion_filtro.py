# -*- coding: utf-8 -*-
"""

FUNCIÓN FILTRO

Created on Tue Jan 21 22:10:17 2020

@author: David

"""
#Programa que separa los números pares de los impares

#Lista a evaluar:

lista =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
impar = filter(lambda x:x % 2,lista)
par = filter(lambda x:x % 2 == 0,lista)
print(list(par))