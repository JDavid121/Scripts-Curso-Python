# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 00:58:23 2020
Evaluación del programa es un año bisiesto

@author: David
"""

def isYearLeap(año):
    #Función que determina si un año es bisiesto
    #año = input("Ingrese el año a evaluar\n\t")
    año=int(año)
    if (año % 400) == 0:
        print("El año",año,"es bisiesto")
        return True
    if (año % 4) == 0: #Averigua si hay residuo
        if (año % 100) == 0:
            print("El año",año,"NO es bisiesto")
            return False
        else:    
            print("El año",año,"es bisiesto")
            return True
    else:    
        print("El año",año,"NO es bisiesto")
        return False
#*************************************************
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")

