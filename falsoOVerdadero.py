#!/usr/bin/env python 3.7
'''
    Julianv
    12/10/2019
    Ingresar el nombre y edad de dos usuarios
    y mostrar en pantalla si son iguales.
'''
usuarioUno = input("Cual es tu nombre: ")
edad_usuario_uno = int(input("Edad: "))
usearioDos = input("Cual es tu nombre: ")
edad_usuario_dos = int(input("Edad: "))

print(f"Tienen las misma edad los usuarios: {edad_usuario_uno == edad_usuario_dos}")

