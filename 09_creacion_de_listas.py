"""

Programa de creación de listas con los datos de una lista
Objetivo: crear una lista con los datos de una lista que
se utilicen como fuente

"""
devices=["ra","rb","rc","sa","sb","sc"]         #Lista original de datos
switches=[]                                     #Creamos una lista vacía, en la que añadiremos los datos buscados
for item in devices:                            #apuntamos al contenido de la lista devices.
    if "s" in item:                             #si "s" se encuentra en un elemento de la lista devices ejecutar
        switches.append(item)                   #append: extrae el elemento apuntado por el lazo for de la lista
                                                #y lo guarda en la lsita switches
print(devices)
print()
print(switches)
