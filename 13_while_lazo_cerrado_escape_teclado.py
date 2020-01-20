"""

Programa ingresar cuatro datos
Objetivo: El programa incrementa una variable
hasta alcanzar su valor máximo.
Se utiliza while en lazo cerrado
con escape por teclado
Elaborado por:
David Jara
17 enero 2020

"""

"""
    Pedir el dato de nombre, apellido, equipo, edad y concatenar los datos en un string.
    Si edad <18 entonces poner: nombre, es menor de edad.
    Si 18<edad<=24 entonces poner: nombre, es juvenil.
    Si edad>24 entonces imprimir: nombre, es senior.
"""

#Programa para ingresar cuatro datos en forma cíclica:

#definición de variables
print("*************************")
print()
while True:
    print("")#indexación del lazo while
    print("Programa que ingresa datos")
    print("Si desea salir ingresar en nombre la letra q")
    print()
    nombre=input("ingresar el primer nombre\n\t") #Ingreso de nombre.
    if nombre == "q":                       # Rutina que permite salir del lazo while.
        print()
        print("Fin del programa")
        break                               # Salida del lazo while.
    apellido=input("ingresar el apellido\n\t")          #Ingreso de datos
    equipo=input("ingresar su equipo favorito\n\t")
    edad=input("ingresar su edad\n\t")
    print("***********************")
    print()
    print("Tu nombre es "+nombre+"\nTu apellido es "+apellido+"\nTu equipo es "+equipo+"\nTu edad es "+edad) #Concatenación de datos.
    edad=int(edad)
    
    if edad<18: #Discriminación deacuerdo a la edad
        print()
        print(nombre,"es","Menor de edad")
    if edad>18 and edad<=24:
        print(nombre,"es","Juvenil")
    if edad>24:
        print(nombre,"es","Senior")
