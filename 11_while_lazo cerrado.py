
"""

Programa contador de números
Objetivo: El programa incrementa una variable
hasta alcanzar su valor máximo.
Se utiliza while en lazo cerrado
Elaborado por:
David Jara
17 enero 2020

"""
print("programa que cuenta hasta llegar a un límite")
x=input("Ingrese el límite de la cuenta\n\t")   #Ingreso del limite de la cuenta.
x=int(x)                                        #Transformamos x a integer
y=1
while True: # while, se ejecuta en lazo cerrado, se utiliza en especial en sensores. 
    print(y,end=" ")
    y=y+1
    if y>x: #(a):condición para salir del lazo while
        break #Si se cumple la condición (a),entonces sale del lazo while.
