"""

Evaluación de la función if y elif

Realizado por: David Jara.
Fecha: 17 enero de 2020
"""

#Código para el uso de if y elif
ac1Num=10
if ac1Num>=1 and ac1Num<=99:            # Sentencia if que evalua (a): 1 <= ac1Num <= 99
    print("This is a standard IPv4")    #Si ac1 cumple con (a) entonces imprime
elif ac1Num >=100 and ac1Num<= 199:     #Si se evalúa (b): 100 <= ac1Num <= 199
        print("this is a extended IPv4 ACL.")   #Si se cumple (b), imprimir.
else:                                   #Si (a) y (b) no se cumplen, entonces:
    print("This is not a standard or extended IPv4 ACL") #Imprimir
