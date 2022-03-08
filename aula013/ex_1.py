"""
Dado um número inteiro positivo n,
calcular a soma dos n primeiros números inteiros positivos.
"""
N = 10

cont: int = 0
sum_values: int = 0

while cont < N:
    value = int(input("Digite um valor: "))
    if value >= 1:
        sum_values += value
    cont += 1

print(sum_values)
