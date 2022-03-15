"""
Faça um programa que leia dez conjuntos de dois valores,
o primeiro representando o número do aluno e o segundo representando a sua
altura em metros. Encontre o aluno mais alto e o mais baixo.
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com
suas alturas.
"""
num = float(input("Digite o número do aluno 1: "))
height = float(input("Digite a altura do aluno 1: "))

greater_num = lesser_num = num
greater_height = lesser_height = height

for i in range(2, 5):
    num = float(input(f"Digite o número do aluno {i}: "))
    height = float(input(f"Digite a altura do aluno {i}: "))

    if height > greater_height:
        greater_height = height
        greater_num = num

    if height < lesser_height:
        lesser_height = height
        lesser_num = num

print(f"O maior aluno {greater_num} altura {greater_height}")
print(f"O menor aluno {lesser_num} altura {lesser_height}")
