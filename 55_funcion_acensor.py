# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 19:24:01 2020

Creación de la clase Ascensor

@author: David
"""

floor_types = ['Estacionamiento', 'Negocios', 'Área de restaurantes', 'Oficinas'] 
floors_numbers = list(range(-1,4))
floor_types
floors_numbers

# Code cell 17
class Elevator:
    
    #Definición de métodos (funciones) de la clase "Elevador"
    #El primer parámetro de un método siempre debe ser "self"
    
    def __init__(self, floors_numbers, floor_types):
        self._floors_numbers = floors_numbers #Variable de entrada floors_numbers[-1,0,1,2]
        self._floor_types = floor_types       #variable de entrada floor_types['Estacionamiento'...'Oficinas']
        self._number_to_type_dict = dict(zip(floors_numbers, floor_types))
                                    #{-1: 'Estacionamiento',0: 'Negocios',1: 'Área de restaurantes',2: 'Oficinas'}
            
        self._type_to_number_dict = dict(zip(floor_types, floors_numbers))
                                    #{'Estacionamiento': -1,'Negocios': 0,'Área de restaurantes': 1,'Oficinas': 2}
        
    def ask_which_floor(self, floor_type): #Método (función) con referencia al "piso" del Ascensor
                                           #Devuelve el número del piso.
        if floor_type in self._floor_types:
            print('The {} floor is the number: {}.'.format(floor_type, self._type_to_number_dict[floor_type]))
        else:
            print('There is no {} floor in this building.'.format(floor_type))
    
    def go_to_floor(self, floors_numbers): #Método con referencia al número del piso del Ascensor.
        if floors_numbers == 3:
            print('There is no {} number in this building.'.format(floors_numbers))
        if floors_numbers in self._floors_numbers:
            print('The {} number is the floor: {}.'.format(floors_numbers, self._number_to_type_dict[floors_numbers]))
        else:
            print('There is no {} number in this building.'.format(floors_numbers))
        
    pass #Fin de la clase ascensor
e1 = Elevator(floors_numbers, floor_types)
#e1.go_to_floor(2)
#el.ask_which_floor('Oficinas')
