"""

Programa contador de números
Objetivo: El programa incrementa una variable
hasta alcanzar su valor máximo 
como entrada.
Elaborado por:
David Jara
17 enero 2020

"""


x=input("Ingrese el límite de la cuenta\n\t")   #Ingreso del número para contar.
x=int(x)                                        #El ingreso del dato es string, para la cuenta
                                                #Se necesita transformar el dato string a integer
y=1                                             #Asignamos un valor inicial al contador y
while y<=x:                                     #Mientras y sea menor o igual a x, ejecutar:
    print(y,end=" ")                            #Imprimimos y, end sirve para concatenar los datos en forma horizontal
    y=y+1                                       #Incrementamos el valor del contador
