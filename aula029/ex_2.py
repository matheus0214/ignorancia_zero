"""
Escreva um programa que recebe uma lista de números até que seja dada a entrada
-1, e depois imprima todos os números pares da sequência que são pares.
"""

NUMBERS = []

num = int(input("Informe um número: "))

while num != -1:
    NUMBERS.append(num)

    num = int(input("Informe um número: "))

for i in NUMBERS:
    if i % 2 == 0:
        print(i)
