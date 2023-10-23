# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:03:55 2023

@author: Alumno
"""

def registrar():
    print("Has seleccionado Registrar")

def eliminar():
    print("Has seleccionado Eliminar")

def editar():
    print("Has seleccionado Editar")

def listar():
    print("Has seleccionado Listar")

# Loop del menú
while True:
    print("Menú Opciones")
    print("1. Registrar")
    print("2. Eliminar")
    print("3. Editar")
    print("4. Listar")
    print("5. Salir")

    opcion = input("Selecciona una opción ")

    if opcion == "1":
        registrar()
    elif opcion == "2":
        eliminar()
    elif opcion == "3":
        editar()
    elif opcion == "4":
        listar()
    elif opcion == "5":
        print("Saliendo del programa")
        break
    else:
        print("Opción no válida.  selecciona una opción válida")