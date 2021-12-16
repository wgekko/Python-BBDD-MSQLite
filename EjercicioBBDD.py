#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 22:44:59 2021

@author: walter
"""

## ejercicio de BBDD  con mqlite
## haciendo CRUD
#
#import sqlite3
#
#miConexion=sqlite3.connect("PrimeraBase")
#miCursor=miConexion.cursor()
#
##miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ART VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(25))")
##miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15,'DEPORTES')")
#
##--------------------------------------------------------------------------------
## INSERTAR DATOS A LA BASE DE DATOS EN FORMA MULTIPLE
##variosProductos=[
##        ("Camiseta",10,"Deportes"),
##        ("Jarrón ",90,"Cerámico"),
##        ("Camión",20,"Juguetería "),
##        ("Auto ",12,"Juguetería"),
##        ("Medias",8,"Deportes"),
##        ("Platos ",34,"Bazar"),
##        ("Vasos",18,"Bazar"),
##        ("PortaRetraros ",20,"Cerámico"),
##        ("Cubiertos ",45,"Bazar "),
##        ("Muñecas",24,"Jugueteria")
##        ]
##miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)
#
##------------------------------------------------------------------
## INSERTAR LOS DATOS A LA BASE DE DATOS EN FORMA INDIVIDUAL 
##miCursor.execute("INSERT INTO PRODUCTOS VALUES('Camiseta',10, 'Deportes')")
##miConexion.commit()
##miCursor.execute("INSERT INTO PRODUCTOS VALUES('Jarrón',90,'Cerámico')")
##miConexion.commit()
##miCursor.execute("INSERT INTO PRODUCTOS VALUES('Camión',20,'Juguetería')")
##miConexion.commit()
##miCursor.execute("INSERT INTO PRODUCTOS VALUES('Auto',12,'Juguetería')")
##miConexion.commit()
##miCursor.execute("INSERT INTO PRODUCTOS VALUES('Medias',8,'Deportes')")
##miConexion.commit()
##miCursor.execute("INSERT INTO PRODUCTOS VALUES('Platos',34,'Bazar')")
##miConexion.commit()
##miCursor.execute("INSERT INTO PRODUCTOS VALUES('Vasos',18,'Bazar')")
##miCursor.execute("INSERT INTO PRODUCTOS VALUES('PortaRetraros',20,'Cerámico')")
##miConexion.commit()
##miCursor.execute("INSERT INTO PRODUCTOS VALUES('Cubiertos',45,'Bazar')")
##miConexion.commit()
##miCursor.execute("INSERT INTO PRODUCTOS VALUES('Muñecas',24,'Jugueteria')")
##miConexion.commit()
#
## LISTAR TODOS LOS PRODUCTOS -----------------------------------------------
#miCursor.execute("SELECT * FROM PRODUCTOS")
#
#ListaProd=miCursor.fetchall()
#print(" *** Lista de Productos *** ")
#print("----------------------------")
#for prod in ListaProd:
#    print(" Producto : ", prod[0], "\n precio : ", prod[1], "\n Sección :", prod[2] )
#    print("---------------------------")
#
#
#miConexion.commit()
#
#miConexion.close()

