#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 23:37:56 2021

@author: ianhj
"""
import usuario # Es una funcion que se realizo para comprobar que es un usuario valido
import password # Se realizo una funcion para que se registre un password valido 
import funcion as fu # El donde se realizaron los calculos 
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors

# y la funcion para ordenar y clasificar lo solicitado 
  
contrasenia_administrativa="user#123A" # Contrasena que viene por default 
nombre_administrativa="Usuario123A" # Nombre que esta delimitada por default 
contrasenia=[]
nombre=[] 
ans=True
f=0
errores=0
Categoria=[] 
Ventas=[] 
Sales_Top=[] 
Producto=[]
Bus_Top=[] 
Producto_Bus=[]
ranking=[]
producto_ranking=[]
mes_venta=[]
especie=[]
stack=[]
Categoria2=[]

while ans: # Menu de opciones que inicializa el programa 
    print("""
    1.Registar como invitado
    2.Iniciar sesion 
    3.Exit/Quit
    """)
    ans = input("\n\t Ingrese la opcion deseada: ")
    
#    Usuario por default: 
#    Nombre_usuario="Usuario123A"
#    Password_usuario="user#123A")
    if ans=="1":
        
        correcto=False # Variable para definir el ciclo se inicia en registro usuario
        while correcto==False:
                nombre=input("Ingrese nombre de usuario: ")
                if usuario.nickname(nombre) == True:
                    print("Usuario creado exitosamente")
                    correcto=True
        
        while correcto==True: #Define Password y lo manda a la funcion correspondiente 
            contrasenia=input("Ingrese su Password: ")
            if password.clave(contrasenia)==True:
                print("Contraseña creada exitosamente")
                correcto=False
                
    elif ans=="2":
        while ans:#Muestra la segunda opcion del menu que es mostrar el reporte
            User_usuario=input("\n\t Ingrese usuario: ")
            password_User = input("\n\t Ingrese contraseña: ")
            #Puede brindarnos la condicion de un registro por default que nos 
            # muestra al inicio o una generado se borra al finalizar sesion
            if ((password_User==contrasenia and User_usuario==nombre) or (password_User==contrasenia_administrativa and nombre_administrativa==User_usuario)):
                print("\n\t Entrando ")
                print("\n\t Generando reporte ")
                print("\n\t Acontinuacion se presentan los productos con mayores ventas: ")
                
                # En las siguientes funciones solo se llaman a las listas y dar una forma de leer mas optima 
                for i in range(50):
                    a=fu.top_sales[i][0]
                    b=fu.top_sales[i][1][1]
                    print([i+1]," Ventas:",a,"Producto:",b)
                    if a>10:
                        Sales_Top.append(a)
                        Producto.append(b)
                    
                print("\n\t Acontinuacion se presentan los productos con mayores ventas por categoria: ")
                
                for i in range(1, 13, 2):
                    a=fu.categories[i]
                    b=fu.categories[i+1]
                    print("\n\t Categoria ",a," Ventas ",b)
                    Categoria.append(a)
                    Ventas.append(b)
                    
                print("\n\t Acontinuacion se presentan los productos con mayores busquedas: ")
                
                for i in range(97):
                    a=fu.top_searches[i][0]
                    b=fu.top_searches[i][1][1]
                    print([i+1],"\n\t No.Busqueda: ",a," Producto:",b)
                    if a>27:
                        Bus_Top.append(a)
                        Producto_Bus.append(b)
           
                print("\n\t Mejores reseñas: ")
                for i in range(20):
                    a=fu.top_rank[i][0]
                    b=fu.top_rank[i][1][1]
                    print([i+1]," Reseñas",a," Producto",b)   
                    
                    
                print("\n\t Peores reseñas: ")
                
                for i in range(20):
                    print([i+1]," Reseñas",fu.less_rank[i][0]," Productos",fu.less_rank[i][1][1])   
                    
                print("\n\t Ventas totales: ",fu.sales_netas_total)
                
                print("\n\t Venta mensual: ")
                for i in range(12):  
                    a=fu.mes_sales_netas[i][1]
                    b=fu.mes_sales_netas[i][0]
                    print("\n\t Mes: ",a,"Ventas: ",b)
                    if b>0:
                        mes_venta.append(a)
                        especie.append(b)
                        
                
                print("\n\t Productos con mas devoluciones: ")
                for i in range(7):  
                    a=fu.top_devoluciones[i][0]
                    b=fu.top_devoluciones[i][1][1]
                    print([i+1],"\n\t No.Devoluciones:: ",a," Producto:",b)
                    
                ans = None
                
                normdata = colors.Normalize(min(Sales_Top), max(Sales_Top))
                colormap = cm.get_cmap("Blues")
                colores =colormap(normdata(Sales_Top))
                
                plt.pie(Sales_Top, labels=Producto, autopct="%0.1f %%", colors=colores)
                plt.axis("equal")
                plt.show()
                
               
                normdata = colors.Normalize(min(Ventas), max(Ventas))
                colormap = cm.get_cmap("Blues")
                colores =colormap(normdata(Ventas))
                
                plt.pie(Ventas, labels=Categoria, autopct="%0.1f %%", colors=colores)
                plt.axis("equal")
                plt.show()
                
                normdata = colors.Normalize(min(Bus_Top), max(Bus_Top))
                colormap = cm.get_cmap("Blues")
                colores =colormap(normdata(Bus_Top))
                
                plt.pie(Bus_Top, labels=Producto_Bus, autopct="%0.1f %%", colors=colores)
                plt.axis("equal")
                plt.show()
                
                normdata = colors.Normalize(min(especie), max(especie))
                colormap = cm.get_cmap("Blues")
                colores =colormap(normdata(especie))
                
                plt.pie(especie, labels=mes_venta, autopct="%0.1f %%", colors=colores)
                plt.axis("equal")
                plt.show()
                
                for i in range(len(fu.top_rank)-1):
                    a=fu.top_rank[i][0]
                    b=fu.top_rank[i][1][1]
                    ranking.append(a)
                    producto_ranking.append(b)
                
                plt.hist(ranking)
                plt.show()
                
                print("\n\t Acontinuacion stack categoria:")
                
                for i in range(1, 13, 2):
                    a=fu.categories2[i]
                    b=fu.categories2[i+1]
                    print("\n\t Categoria ",a," Stack ",b)
                    Categoria2.append(a)
                    stack.append(b)
                
                normdata = colors.Normalize(min(stack), max(stack))
                colormap = cm.get_cmap("Blues")
                colores =colormap(normdata(stack))
                
                plt.pie(stack, labels=Categoria2, autopct="%0.1f %%", colors=colores)
                plt.axis("equal")
                plt.show()
                
                plt.hist(stack)
                plt.show
                
            else: # Funcion que delimita los errores a cinco y si esto ocurre cierra el programa 
                errores+=1
                print("\n\t Intentos fallidos",errores)
                if errores==5:
                          print("\n Goodbye") 
                          ans = None
         
    elif ans=="3": # Ultima opcion sirve para terminar con el programa es la ultima opcion del menu 
      print("\n Goodbye") 
      ans = None
    else: # Condiciona que solo se pueda seleccionar una de las tres opciones pre estrablecidas 
       print("\n Es una opcion no valida")
