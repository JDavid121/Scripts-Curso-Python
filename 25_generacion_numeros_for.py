# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 17:52:29 2020

@author: David
"""

"""
Generación de números con lazo FOR

"""
def headline():
    print("******************************************************")
    print()
def endline():
    print()
    print("******************************************************")
    
    
#1.0 Primera forma:
headline()
for i in range(10):  #genera 10 números desde i=0
    print(i,end=" ")         #hasta i=9, imprime el valor de i
endline()

#2.0 Segunda forma:
headline()
for i in range (1,20): #Genera una lista de números del 1 al 19
    print(i,end=" ")
endline()

#3.0 Tercera forma
headline()
for i in range(30,0,-1): #range=rango (vinicial,vfinal,variación)
    print(i,end=" ")
endline()