#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 23:39:08 2021

@author: ianhj
"""

def clave(password):

        validar=False #que se vayan cumpliendo los requisitos uno a uno.
        long=len(password) #Calcula la longitud de la contraseña
        espacio=False  #variable para identificar espacios
        mayuscula=False #variable para identificar letras mayúsculas
        minuscula=False #variable para contar identificar letras minúsculas
        numeros=False #variable para identificar números
        y=password.isalnum()#si es alfanumérica retona True
        correcto=True #verifica que hayan mayuscula, minuscula, numeros y no alfanuméricos
        
        for carac in password: #ciclo for que recorre caracter por caracter en la contraseña

            if carac.isspace()==True: #Saber si el caracter es un espacio
                espacio=True #si encuentra un espacio se cambia el valor user

            if carac.isupper()== True: #saber si hay mayuscula
                mayuscula=True #acumulador o contador de mayusculas
                
            if carac.islower()== True: #saber si hay minúsculas
                minuscula=True #acumulador o contador de minúsculas
                
            if carac.isdigit()== True: #saber si hay números
                numeros=True #acumulador o contador de numeros
                            
        if espacio==True: #hay espacios en blanco
                print("La contraseña no puede contener espacios")
        else:
            validar=True #se cumple el primer requisito que no hayan espacios
                       
        if long <8 and validar==True:
            print("Mínimo 8 caracteres")
            validar=False #cambia a Flase si no se cumple el requisito móinimo de caracteres

        if mayuscula == True and minuscula ==True and numeros == True and y== False and validar ==True:
           validar = True #Cumple el requisito de tener mayuscula, minuscula, numeros y no alfanuméricos
        else:
           correcto=False #uno o mas requisitos de mayuscula, minuscula, numeros y no alfanuméricos no se cumple
           
        if validar == True and correcto==False:
           print("La contraseña elegida no es segura: debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")

        if validar == True and correcto ==True:
           return True

