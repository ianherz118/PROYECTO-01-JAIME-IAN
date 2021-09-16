#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 23:38:36 2021

@author: ianhj
"""

def nickname(nombre_usuario):

        long=len(nombre_usuario) #Calcular la longitud del nomre de usuario
        y=nombre_usuario.isalnum() #Calcula que la cadena contenga valores alfanuméricos
        
        if y== False: # La cadena contiene valores no alfanuméricos
            print("El nombre de usuario puede contener solo letras y números")
            
        if long < 6: 
            print("El nombre de usuario debe contener al menos 6 caracteres")
            
        if long > 12: 
            print("El nombre de usuario no puede contener más de 12 caracteres")
            
        if long >5 and long <13 and y ==True:
            return True #Verdadero si el tamaño es mayor a 5 y menor a 13