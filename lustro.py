#!/usr/bin/env python 3.7
'''
    JulianV
    12/10/2019
    Cantidad de segundos en un lustro.
'''
print()
print("un minuto tiene 60 segundos")
print("Una hora tiene 60 min * 60 seg = 3600 segundos.")
print("Un dia tiene 24 hrs. * 3600 seg = 86400")
print("------------------------------------------------")
print("Un lustro equivale a 5 años.")
print("Un año en promedio tiene 365 dias.")

DIASENUNAŇO = 365   # dias en promedio
segundos_en_dia = 24 * 3600
segundos_en_un_año = DIASENUNAŇO * segundos_en_dia
segundos_en_lustro = 5 * segundos_en_un_año

print('Basado en la relacion anterior y los promedios que \
habria en cada hora, dia y año el resultado es el siguiente.')

print(f"\nLos segundos que habrian en un lustro son: {segundos_en_lustro} segundos\n")
