# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 01:10:56 2020

@author: David
"""

# Code cell 15
floor_types = ['Parking', 'Shops', 'Food Court', 'Offices']
floors_numbers = range(-1,3)
#elevator_dict = dict(...)
zip(floors_numbers,floor_types)
z = list(zip(floors_numbers,floor_types))
print (z)     
elevator_dict = dict(zip(floors_numbers,floor_types))
print(elevator_dict)
