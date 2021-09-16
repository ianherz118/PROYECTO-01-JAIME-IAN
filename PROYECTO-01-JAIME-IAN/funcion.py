#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 23:51:19 2021
@author: ianhj
"""
import lifestore_file as li # Importa las variales y nos permite reducir su nombre para no escribir todo 
# Declaracion de variables que se usaran las letras son contadores y lo demas listas 
a=0
z=1
zw=1
w=0
top_searches=[]
top_sales=[]
sales_netas=[]
prom=0
le=len(li.lifestore_products)+1
rank=[]
zz=0
categories=[]
categories2=[]
g=0
acategoria=0
top_sales_netas=[]
sales_netas_total=[]
wf=0
xf=0
fechas=["/01/","/02/","/03/","/04/","/05/","/06/","/07/","/08/","/09/","/10/","/11/","/12/"]
o=0
rank_devoluciones=[]
top_devoluciones=[]
stack=0

def selectionSort(aList): # Funcion realizada para ordenar listas generadas 
    for i in range(len(aList)):
        least = i
        for k in range(i+1, len(aList)):
            if aList[k] < aList[least]:
                least = k
                 
        swap(aList, least, i)
         
def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

while z<le: #Operacion que se realiza para clasificar ventas por productos 
    for i in range (len(li.lifestore_sales)):    
        if li.lifestore_sales[i][1]==z:
            prom=li.lifestore_sales[i][2]+prom
            w+=1
    if w!=0: # Se usa un condicional para que cuando sea cerro no se indetermine 
        prom=round(prom/w,2)
        rank.append([prom,li.lifestore_products[z-1]])    
    else:
        rank.append([prom,li.lifestore_products[z-1]])   
    top_sales.append([w,li.lifestore_products[z-1]]) #Agregamos el elemento total de ventas
    #Tecnicamente las que son ceros no existirian como ventas pero se conservaron
    #porque en las indicaciones no era un factor de discriminacion 
    
    w=0
    z+=1    
    prom=0
# Ordenar la lista y reordenarla para el caso de que en lugar de top sean los que menos elementos 
selectionSort(top_sales)
top_sales=top_sales[::-1]
less_sales=top_sales[::-1]

rank.sort()
top_rank=rank[::-1]
less_rank=top_rank[::-1]

while zz<le: # Algoritmo para identificar el numero de busquedas realizadas por objeto
    for i in range (len(li.lifestore_searches)):    
        a=li.lifestore_searches.count([i,zz])+a
    top_searches.append([a,li.lifestore_products[zz-1]])
    a=0
    zz+=1    
selectionSort(top_searches)# Se utiliza igual que el anterior se reordena y se hace top de mejores y peores 
top_searches=top_searches[::-1]
less_searches=top_searches[::-1]

for i in range(le-2): #Funcion para identificar cuantas categorias de producto hay 
    if(top_sales[i][1][3]!=top_sales[i+1][1][3]):
        categories.extend([top_sales[i][1][3]])
        
        
unique_categories = list(dict.fromkeys(categories)) # Se usa para eliminar valores que se repiten 

categories.clear() # la borramos esta lista para reuzarla despues  
leca=len(unique_categories)-1
while g<leca+1: #Se hace la sumatoria de ventas por especie y no de forma neta
    for i in range(le-1):
        if(top_sales[i][1][3]==unique_categories[g]):
            acategoria=top_sales[i][0]+acategoria
    categories.append(acategoria)
    categories.extend([unique_categories[g]])
    g+=1
    acategoria=0
g=0
while g<leca+1: #Se hace la sumatoria de ventas por especie y no de forma neta
    for i in range(le-1):
        if(top_sales[i][1][3]==unique_categories[g]):
            # acategoria=top_sales[i][0]+acategoria
            stack=top_sales[i][1][4]+stack
    categories2.append(stack)
    categories2.extend([unique_categories[g]])
    g+=1
    stack=0
    
while o<12: #Se hace la clasificacion de por fechas usando una lista fechas para ordenar y clasificar 
    for i in range (len(li.lifestore_sales)):  
        if li.lifestore_sales[i][4]==0:
            index=li.lifestore_sales[i][3].find(fechas[o]) # Se usa find para encontra la cadena y reconozca fechas 
            if index==2:
                wf+=1
    sales_netas.append([wf,fechas[o]]) #Agrega al vector y finalizamos 
    xf=wf+xf
    wf=0
    o+=1    
zf=0
wff=0
promf=0

while zf<le: # Es una funcion para discriminar por venta pero sin devoluciones 
        for i in range (len(li.lifestore_sales)):    
            if li.lifestore_sales[i][1]==zf and li.lifestore_sales[i][4]==1: #Condicional para quitar devoluciones 
                promf=li.lifestore_sales[i][2]+promf
                wff+=1
        if wff!=0: #SE generara una lista de devoluciones buscando encontrar algo significativo 
            promf=round(promf/wff,2)
            rank_devoluciones.append([promf,li.lifestore_products[zf-1]])    
        else:
            rank_devoluciones.append([promf,li.lifestore_products[zf-1]])   
        top_devoluciones.append([wff,li.lifestore_products[zf-1]]) 
        wff=0
        zf+=1    
        promf=0

selectionSort(top_devoluciones) # Se hizo lo mismo que los anteriores solo se ordena y se llama a la funcion que se 
#realizo 
top_devoluciones=top_devoluciones[::-1]
less_devoluciones=top_devoluciones[::-1]

sales_netas_total=xf  # Se hizo lo mismo que se ha realizado en los anteriores top 
selectionSort(sales_netas)
mes_sales_netas=sales_netas[::-1]
mes_less_sales_netas=mes_sales_netas[::-1]

