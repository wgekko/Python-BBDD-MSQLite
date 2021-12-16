#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 00:27:03 2021

@author: walter
"""

# ejercicio de BBDD  con mqlite
## haciendo CRUD

import sqlite3

# creo la base de datos -------
miConexion=sqlite3.connect("GestorProd")
miCursor=miConexion.cursor()

# trabajamos con BBDD con primary key autoincremental
#miCursor.execute('''CREATE TABLE PRODUCTOS ( ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_ART VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(25))''')

##------------------------------------------------------------------
## INSERTAR LOS DATOS A LA BASE DE DATOS EN FORMA INDIVIDUAL

#miCursor.execute("INSERT INTO PRODUCTOS VALUES(1,'Balon',15, 'Deportes')")
#miConexion.commit() 
#miCursor.execute("INSERT INTO PRODUCTOS VALUES(2,'Camiseta',10, 'Deportes')")
#miConexion.commit()
#miCursor.execute("INSERT INTO PRODUCTOS VALUES(3,'Jarrón',90,'Cerámico')")
#miConexion.commit()
#miCursor.execute("INSERT INTO PRODUCTOS VALUES(4,'Camión',20,'Juguetería')")
#miConexion.commit()
#miCursor.execute("INSERT INTO PRODUCTOS VALUES(5,'Auto',12,'Juguetería')")
#miConexion.commit()
#miCursor.execute("INSERT INTO PRODUCTOS VALUES(6,'Medias',8,'Deportes')")
#miConexion.commit()
#miCursor.execute("INSERT INTO PRODUCTOS VALUES(7,'Platos',34,'Bazar')")
#miConexion.commit()
#miCursor.execute("INSERT INTO PRODUCTOS VALUES(8,'Vasos',18,'Bazar')")
#miConexion.commit()
#miCursor.execute("INSERT INTO PRODUCTOS VALUES(9,'PortaRetraros',20,'Cerámico')")
#miConexion.commit()
#miCursor.execute("INSERT INTO PRODUCTOS VALUES(10,'Cubiertos',45,'Bazar')")
#miConexion.commit()
#miCursor.execute("INSERT INTO PRODUCTOS VALUES(11,'Muñecas',24,'Jugueteria')")
#miConexion.commit()


## LISTAR TODOS LOS PRODUCTOS -----------------------------------------------
miCursor.execute("SELECT * FROM PRODUCTOS")

ListaProd=miCursor.fetchall()
print(" *** Lista de Productos *** ")
print("----------------------------")
for prod in ListaProd:
    print(" ID :",prod[0],"\n Producto : ", prod[1], "\n precio : ", prod[2], "\n Sección :", prod[3] )
    print("---------------------------")

miConexion.commit()

## LISTAR TODOS LOS PRODUCTOS  DE UNA SECCION ---------------------------------------
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION ='Deportes'")

ListaProd=miCursor.fetchall()
print(" *** Lista de Productos por Sección *** ")
print("----------------------------")
for prod in ListaProd:
    print(" ID :",prod[0],"\n Producto : ", prod[1], "\n precio : ", prod[2], "\n Sección :", prod[3] )
    print("---------------------------")

miConexion.commit()

## LISTAR TODOS LOS PRODUCTOS  ORDENADOS POR PRECIOS mayor a un valor en forma ascendente--------------
miCursor.execute("SELECT * FROM PRODUCTOS WHERE PRECIO >15 ORDER BY PRECIO ASC")

ListaProd=miCursor.fetchall()
print(" *** Lista de Productos por precio mayor a 15 en forma  ascendente *** ")
print("------------------------------------------------------------------------")
for prod in ListaProd:
    print(" ID :",prod[0],"\n Producto : ", prod[1], "\n precio : ", prod[2], "\n Sección :", prod[3] )
    print("---------------------------")

miConexion.commit()

## LISTAR TODOS LOS PRODUCTOS  ORDENADOS POR PRECIOS en forma descendente------------------------------
miCursor.execute("SELECT * FROM PRODUCTOS WHERE PRECIO >1 ORDER BY PRECIO DESC")

ListaProd=miCursor.fetchall()
print(" *** Lista de Productos por precio en forma descendente *** ")
print("------------------------------------------------------------------------")
for prod in ListaProd:
    print(" ID :",prod[0],"\n Producto : ", prod[1], "\n precio : ", prod[2], "\n Sección :", prod[3] )
    print("---------------------------")

miConexion.commit()

## ACTUALIZAR O MODIFICAR DATOS DE LA TABA DE LA BASE DE DATOS ------------------------------
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=23 WHERE NOMBRE_ART='Balon'")
miCursor.execute("UPDATE PRODUCTOS SET NOMBRE_ART='Maquina Excabadora' WHERE ID=4")

ListaProd=miCursor.fetchall()
miCursor.execute("SELECT * FROM PRODUCTOS")
# muestro por consola la nueva lista de productos actualizada
ListaProd=miCursor.fetchall()
print(" *** Lista de Productos *** ")
print("----------------------------")
for prod in ListaProd:
    print(" ID :",prod[0],"\n Producto : ", prod[1], "\n precio : ", prod[2], "\n Sección :", prod[3] )
    print("---------------------------")

miConexion.commit()

## BORRAR DATOS DE LA TABA DE LA BASE DE DATOS ------------------------------
miCursor.execute("DELETE FROM PRODUCTOS WHERE NOMBRE_ART='Muñecas'") # BORRAR POR NOMBRE
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=11") # BORRAR POR ID 

ListaProd=miCursor.fetchall()
miCursor.execute("SELECT * FROM PRODUCTOS")
# muestro por consola la nueva lista de productos sin los productos eliminados
ListaProd=miCursor.fetchall()
print(" *** Lista de Productos *** ")
print("----------------------------")
for prod in ListaProd:
    print(" ID :",prod[0],"\n Producto : ", prod[1], "\n precio : ", prod[2], "\n Sección :", prod[3] )
    print("---------------------------")

miConexion.commit()


miConexion.close()