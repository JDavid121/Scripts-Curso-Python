# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:11:17 2020

@author: David
"""

#PROGRAMA DE LA CALEFACCIÓN INTELIGENTE

"""
12) Imagine un termostato inteligente conectado a la puerta que pueda
detectar, además de la temperatura, el momento en el que las personas 
entran o salen de la casa.
Escriba una función que, cuando la temperatura sea inferior a 20 ºC y 
haya personas en la casa (codificado como valor booleano que se envía 
como parámetro a la función), inicie la calefacción mediante la devolución 
de la cadena "calefacción encendida". Cuando la temperatura llegue a 23 grados 
o no haya personas en la casa, la función devuelve la cadena 
"calefacción apagada". Cuando no se cumpla ninguna de estas condiciones, 
la función es "No hacer nada".
"""

def smart_thermostat(temp, people_in): #Función termostato inteligente
    
    if people_in == True:
        if temp <20:   
            return "Calefacción Encendida"
        if temp >= 23: #Indica que ya se pasó a calefacción apagada
            return "Calefacción Apagada por exceso Temperatura"
        else:
            return "No Hacer Nada"
    if people_in == False:
        
        return "Calefacción Apagada por falta de personas"
        
            