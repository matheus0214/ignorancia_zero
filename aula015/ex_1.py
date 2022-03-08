"""
Dizemos que um inteiro positivo n é perfeito se for igual à soma de
seus divisores positivos diferentes de n.

Exemplo: 6 é perfeito, pois 1+2+3 = 6.
       Dado um inteiro positivo n, verificar se n é perfeito.
"""
N = int(input("Entre com o valor de N: "))

total: int = 0
cont: int = 1

while cont < N:
    if N % cont == 0:
        total += cont
    cont += 1

if total == N:
    print(f"{N} é perfeito")
else:
    print(f"{N} não é perfeito")
