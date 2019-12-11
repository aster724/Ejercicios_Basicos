#!/usr/bin/env python 3.7
'''
    JulianV
    12/06/2019
    Calcular Dolares a Pesos
    cambiodolar.mx $1 dls -> $19.33 pesos mx.
'''
PESOS_POR_DOLAR = 19.33
print("----------------------------")
print(" -- Tipo de cambio --")
print("$1 dls --> $19.33 pesos mx")
print("----------------------------")
dolares = int(input("Cantidad en numero redondo (no centavos): "))
print(f'Pesos por revir: ${float(PESOS_POR_DOLAR * dolares)}')