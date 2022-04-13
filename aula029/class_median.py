"""Média maior que sete"""

from typing import List


STUDENTS = 10

MEDIANS: List[float] = []

for i in range(1, STUDENTS + 1):
    grades: int = 0

    for j in range(1, 5):
        grades += float(input(f"Digite a nota {j} do aluno {i}: "))

    grades /= 4

    MEDIANS.append(grades)

num: int = 0

for median in MEDIANS:
    if median >= 7.0:
        num += 1

print(f"O número de alunos com média maior que 7.0 é {num}")
