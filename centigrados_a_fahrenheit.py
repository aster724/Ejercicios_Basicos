#!/usr/bin/env python3.7
'''
    JulianV
    12/10/2019
    Convertir grados centigrados a grados
    Fahrenheit.
    La formula que utilizare es la siguiente.
    (0°C × 9/5) + 32 = 32°F
'''
print("Centigrados a Fahrenheit")
print("-------------------------")
centigrados = float(input("\nTemperatura en grados Centigrados --> "))
fahrenheit = (centigrados * 9 / 5) + 32
print(f"\nLa temperatura en {centigrados}℃  equivale a {fahrenheit}℉")