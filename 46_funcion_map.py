# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:08:41 2020

@author: David
"""

sec = ["datos", "sal", "diario", "gato", "perro"]
a=lambda x:sec[x].upper()
#a=sec[0].upper()
print(a)
#porgrama principal
b=len(sec)
c=[]
for i in range(0,b-1,1):
    c.append(a(i))
print (c)
print("*****************************")
b=lambda x:x.upper()
d=map(b,sec)
e=list(d)
print(e)
    