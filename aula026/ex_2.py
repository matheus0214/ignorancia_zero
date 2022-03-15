"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os dois vetores.
"""
from typing import List


even: List[int] = []
odd: List[int] = []

for i in range(1, 21):
    number = int(input(f"Informe o número {i}: "))

    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print(f"Números pares: {even}")
print(f"Números impares: {odd}")
