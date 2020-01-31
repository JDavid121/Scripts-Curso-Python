# -*- coding: utf-8 -*-
"""
Función map()
Created on Wed Jan 22 10:24:46 2020

La función map() retorna un objeto map (el cual es un interacción) del resultado
de aplicar una función a cada ítem de una variable interactuable
(lista, tuple, etc)

Sintaxis.

map(funcion,iteraccion)

Parametros:
funcion: Es una función en la cual se hace un paso (mapeo) en cada elmento
de una variable interactuable.
iteraccion: Es la variable interactuable a ser mapeada.

map() function returns a map object(which is an iterator) of the results after
applying the given function to each item of a given iterable (list, tuple etc.)

Syntax :

map(fun, iter)
Parameters :

Retorno: retorna una lista de resultados después de aplicar la función dada a
cada item de la variable interactuable. (lista, tuple, etc).

Nota: El retorno del valor de map() puede ser utilizado para crear una lista
(con list()) con con la función set()



fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.

Returns :

Returns a list of the results after applying the given function  
to each item of a given iterable (list, tuple etc.)

NOTE : The returned value from map() (map object) then can be passed 
to functions like list() (to create a list), set() (to create a set) .

@author: David
"""
# Python program to demonstrate working 
# of map.
 
# Retorna el valor doble de N  
# Return double of n 

def addition(n): #Definición de la función doble.
    return n + n 
  
# We double all numbers using map() 
numbers = (1, 2, 3, 4) #Variable tuple
result = map(addition, numbers) 
print(list(result))
print("*******************************")
print(set(result))
