# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 18:06:26 2020

@author: David
"""

"""
#Laboratorio: Su tarea es escribir y probar una función que
toma dos argumentos (un año y un mes) y devuelve el número 
de días para el par mes / año dado (aunque solo febrero es 
sensible al valor del año, su función debería ser universal).

"""
def isYearLeap(año):
    #Función que determina si un año es bisiesto
    #año = input("Ingrese el año a evaluar\n\t")
    año=int(año)
    if (año % 400) == 0:
        #print("El año",año,"es bisiesto")
        return True
    if (año % 4) == 0: #Averigua si hay residuo
        if (año % 100) == 0:
            #print("El año",año,"NO es bisiesto")
            return False
        else:    
            #print("El año",año,"es bisiesto")
            return True
    else:    
        #print("El año",año,"NO es bisiesto")
        return False

def daysinmonth(year,month):
    if year <= 0: #Condiciones para el año.
        print("Error año debe ser mayor a 1",end=(" "))
        print("none")
        return "none"
        
    if year >= 2100: #Condciones para el año.
        print("Error año debe ser menor a 2100",end=(" "))
        print("none")
        return "none"
    if month <= 0 or month >=13:
        print("Error mes debe esta comprendio entre 1 y 12",end=(" "))
        print("none")
        return "none"
    
    montht=[31,28,31,30,31,30,31,31,30,31,30,31] #Tabla de números de días por mes
    #isYearLeap(year) #si el año es bisiesto toma el valor True,
                     #si el año no es bisiesto, toma el valor False.
    for i in range (0,13,1):
        if month == i:
            numday=montht[i-1]
            print(numday)
            return numday
        if month == 2 and isYearLeap(year):
            print (29)
            return 29
#***********************************************************
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysinmonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")


