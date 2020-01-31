# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:42:59 2020
Función map()

@author: David
"""

# Sumar dos listas de números utilizando la función lambda y map
number1=[1,2,3,4]
number2=[4,5,6,7]

resultado=map(lambda x,y:x + y,number1,number2)
print(list(resultado))
#OBSERVACIONES
# 1.0 la función lambda se utiliza con dos argumentos lambda x,y
# 2.0 El resultado de la función lambda utiliza los dos argumentos: x + y
# 3.0 Los dos argumentos que necesita la función lambda
# son los argumentos number1,number2

#Sumar tres listas de argumentos utilizando lambda y map
number1=[1,2,3,4]
number2=[4,5,6,7]
number3=[8,9,10,11]

resultado=map(lambda x,y,z:x+y+z,number1,number2,number3)
print(list(resultado))

# PROGRAMA QUE SEPARA VARIABLES STRING EN LETRAS 
palabras = ['sat', 'bat', 'cat', 'mat'] #lista de palabras a separar
  
# map() can listify the list of strings individually 
print("***********************************")
resultado = map(list,palabras)
resultado_lista = list(resultado)
print(resultado_lista)
print("***********************************")
#*******************************************
# Programa que transforma una lista de caracteres en un string
palabra=["s","a","t"]
b="" # string resultado
for i in palabra:
    b = b+i
print (b)
    
