# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:33:51 2023

@author: Alumno
"""

import sqlite3


# Conectar a la base de datos (o crearla si no existe)
conexion = sqlite3.connect("pascacio_almacen.db")

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear la tabla "Producto" si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Producto (
        idproducto INTEGER PRIMARY KEY,
        codigo TEXT NOT NULL,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL
    )
''')


# Guardar los cambios y cerrar la conexión
conexion.commit()
conexion.close()



print("Base de Datos 'pascacio_almacen' y tabla 'Producto' creadas exitosamente.")
