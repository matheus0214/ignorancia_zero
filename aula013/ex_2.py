"""
Dado um número inteiro positivo n, imprimir os n primeiros naturais ímpares.
n = 4 --> 1, 3, 5, 7
n = 3 --> 1, 3, 5
n = 7 --> 1, 3, 5, 7, 9, 11, 13
"""

N = int(input("Entre com o valor de N: "))

cont: int = 0
initial: int = 1

while cont < N:
    print(initial, end=" ")
    initial += 2
    cont += 1
