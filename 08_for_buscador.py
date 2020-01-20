"""

Evaluación del lazo for como buscador

Realizado por: David Jara.
Fecha: 17 enero de 2020
"""
devices=["r1","r2","r3","s1","s2"]      #Definición de la lista devices
for item in devices:                    #Rutina for que apunta a la lista devices
    if "1" in item:                     #busca la letra "r" en cada elemento de la lista devices
        print(item)                     #imprime el dato de la lista solo si la búsqueda es verdadera
