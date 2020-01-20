# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 18:06:26 2020

@author: David
"""

"""

Su tarea es escribir y probar una función que toma 
tres argumentos (un año, un mes y un día del mes) y 
devuelve los días correspondiente del año, o devuelve 
None si alguno de los argumentos es inválido.

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
        
    if year >= 2501: #Condciones para el año.
        print("Error año debe ser menor a 2500",end=(" "))
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
            #print(numday)
            return numday
        if month == 2 and isYearLeap(year):
            #print (29)
            return 29
#***********************************************************

def dayOfYear(year3,month3,day3):   #Función que indica el número días transcurridos
                                    #En el año
    #*******************************************************
    #Evaluación de mensajes de error:
    if isYearLeap(year3): #Prg que arroja error si año es bisiesto y día mayor a 29
        if month3 == 2:
            if day3< 1 or day3 > 29:
                print("ERROR, año bisiesto, ingresar un día comprendido entre 1 y 29")
                return "nope"
        
    if not(isYearLeap(year3)): #Prg arroja error si año no bisiesto y día mayor a 28
        if month3 == 2:
            if day3< 0 or day3 > 28:
                print("ERROR, ingresar un día comprendido entre 1 y 28")
                return "nope"
    
    if year3 < 0 or year3 >=2501: #Error si 1<year3 ó year3 > 2500
        print("ERROR, ingresar un año comprendido entre 1 y 2500")
        return "nope"
    if month3 <1 or month3 >13: #Error si month3<1 ó month3>12
        print("ERROR, ingresar un mes comprendido entre 1 y 12")
        return "nope"
    if day3 < 1 or day3 > 31: #Error si day3<1 o day3>31
        print("ERROR, ingresar un día comprendido entre 1 y 31")
        return "nope"
    
    
    #*******************************************************
    b=0 #Acumulador de números de días por cada mes
    for i in range(1,month3,1): #Desde i=1 hasta month3
        a=daysinmonth(year3,i) # a = num días del mes i
        b=b+a                  # b = acumulador (valor incial 0)
        #print("El número de días por meses es\n\t",b)
    c=b+day3 #Suma los días acumulados en los meses y los días del mes en curso
    #print("El número de días acumulados en los meses es\t",b)
    print("El número total de días acumulados en\nel año",year3,"es",c)
    return c #retorno de la función c
          


