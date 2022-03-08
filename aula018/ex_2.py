"""
Sabe-se que um número da forma n**3 é igual a soma de n ímpares consecutivos.

Exemplo: 1**3= 1, 2**3= 3+5, 3**3= 7+9+11,  4**3= 13+15+17+19,...
Dado m, determine os ímpares consecutivos cuja soma é igual a n**3 para n
assumindo valores de 1 a m.
"""

M = int(input("Informe o valor de M: "))

first: int = 1
total: int = 0
while total != M ** 3:
    total: int = 0

    for n in range(first, M * 2 + first, 2):
        total += n

    if total == M ** 3:
        print(f"{M}**3 = ", end="")
        for n in range(first, M * 2 + first, 2):
            if n != (M * 2 + first) - 2:
                print(f"{n}+", end="")
            else:
                print(n, end="\n")
    first += 2
