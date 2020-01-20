"""

Programa contador de números
Objetivo: El programa incrementa una variable
hasta alcanzar su valor máximo.
Se utiliza while en lazo cerrado
con escape por teclado
Elaborado por:
David Jara
17 enero 2020

"""
#Programa contador
while True:                                     #Lazo while verdadero
    x=input("Ingrese el número a contar\n\t")   #limite de cuenta
    if x == 'q' or x == 'quit':                 #Condición (a): para escapar del lazo while
        print("Fin del programa")
        break                                   #escape del lazo while
    x=int(x)
    y=1                         #definición de la variable y=1
    while True:                 #Lazo while cerrado
        print(y, end=" ")       #imprime el valor de y
        y=y+1                   #incrementa el valor de y
        if y>x:                 #Si y>x (limite de la cuenta)
            print("\n")         #Para que la frase "ingrese el número a contar" empiece en una línea nueva
            break               #sale del lazo while
