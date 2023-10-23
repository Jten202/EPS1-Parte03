# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:03:55 2023

@author: Alumno
"""

import sqlite3

def menu():
    print("Menú Opciones")
    print("1. Registrar")
    print("2. Eliminar")
    print("3. Editar")
    print("4. Listar")
    print("5. Salir")

def registrar():
    print("Has seleccionado Registrar")
    conexion = sqlite3.connect("pascacios_almacen.db")
    cursor = conexion.cursor()
    consulta_Producto="""INSERT INTO 
                        Producto(idproducto,codigo,nombre,precio)
                        VALUES(?,?,?,?)"""
    listar=[(1,'AO1','Lapicero',3.20),
            (2,'A02','Borrador',1.20),
            (3,'A03','Tijera',1.50),
            (4,'A04','Block',5.10),
            (5,'A05','Tiza',0.50),
            (6,'A06','Regla',1.60),
            (7,'A07','Papel',2.60),
            (8,'A08','Goma',2.50),
            (9,'A09','Plumon',3.10),
            (10,'A10','Cinta',4.10)]
    cursor.executemany(consulta_Producto,listar)
    conexion.commit()
    conexion.close()
    
def eliminar():
    print("Has seleccionado Eliminar")
    conexion = sqlite3.connect("pascacios_almacen.db")
    cursor = conexion.cursor()
    idproducto = input("ID del producto a eliminar: ")
    consulta = "DELETE FROM Producto WHERE idproducto = ?"

    try:
        cursor.execute(consulta, (idproducto,))
        conexion.commit()
        print("Producto eliminado con éxito.")
    except sqlite3.Error as e:
        print("Error al eliminar el producto:", e)
    finally:
        conexion.close()
    
def editar():
    print("Has seleccionado Editar")
    conexion = sqlite3.connect("pascacios_almacen.db")
    cursor = conexion.cursor()
    idproducto = int(input("ID del producto a editar: "))
    codigo = input("Nuevo código: ")
    nombre = input("Nuevo nombre: ")
    precio = float(input("Nuevo precio: "))

    consulta = """UPDATE Producto
                  SET codigo=?, nombre=?, precio=?
                  WHERE idproducto=?"""
    try:
        cursor.execute(consulta, (codigo, nombre, precio, idproducto))
        conexion.commit()
    except sqlite3.Error as e:
        print("Error al editar el producto:", e)
    finally:
        conexion.close()
    
def listar():
    print("Has seleccionado Listar")
    conexion = sqlite3.connect("pascacios_almacen.db")
    cursor = conexion.cursor()
    listar="SELECT * FROM Producto"
    cursor.execute(listar)
    Productos=cursor.fetchall()
    print("ID\tNombre\tDescripcion\tPrecio")
    for producto in Productos:
        id_producto, nombre, descripcion, precio = producto
        print(f"{id_producto}\t{nombre}\t{descripcion}\t{precio}")
    conexion.close()

def error():
    print("Opción incorrecta")
    
def salir():
    print("Gracias por su visita....")

# Loop del menú
opcion = 1
while opcion!=5:
  menu()
  opcion = int(input("opcion: "))
  if opcion == 1:
     registrar()
  elif opcion == 2:
     eliminar()
  elif opcion == 3:
     editar()
  elif opcion == 4:
     listar()
  elif opcion == 5:
     salir()
  else:
     error()
