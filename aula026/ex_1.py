"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

from typing import List


grades: List[float] = []
total: float = 0

for i in range(1, 5):
    grade = float(input(f"Informe a nota {i}: "))

    grades.append(grade)

for i in range(4):
    total += grades[i]

print(f"Média das notas {total/4}")
