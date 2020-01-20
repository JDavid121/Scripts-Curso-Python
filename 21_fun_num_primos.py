# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 20:32:05 2020

@author: David Jara
"""
"""
Programa para comprobar si un número es primo
"""
def numPrim(x): #Función que evalúa si x es un número primo.
    #Valor de error
    #x=input("Ingresar el número a evaluar\n\t")
    x=int(x) #Transforma x a integer
    if x == 1: #Evalúa si 1 es primo o no (se decide que no)
        print("\t",x,"no es un numero primo")
        return False
    if x == 2: #Evalúa si 2 es primo (sí es primo)
        print("\t",x,"es un número primo")
        return True
    if x >= 3: #para números mayores o iguales a 3, evaluar
        for i in range(2,x,1): #desde i=2, hasta x, en pasos de 1:
            a=x%i              #Calcula el residuo de dividir x para
                               #la serie 1,2,...x
            #print(a,end=" ")
            #print(i)
            if a == 0: #Si el residuo es cero, x no es primo
                print("\t",x,"no es un número primo")
                return False
                break
        print("\t",x,"es un número primo") #Si se evalúa a para todos los
        return True                        # valores de i desde 2 hasta x (lazo for)
                                           # y ninguno da a=0, entonces x
                                          # es primo