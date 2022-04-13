"""
Escreva um programa que crie uma lista de elementos, até se entrar -1,
e depois imprima todos os números da lista que são maiores que 10.
"""
NUMBERS = []

num = int(input("Informe um número: "))

while num != -1:
    NUMBERS.append(num)

    num = int(input("Informe um número: "))

for i in NUMBERS:
    if i > 10:
        print(i)
