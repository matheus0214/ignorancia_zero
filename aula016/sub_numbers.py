""" Sub numbers """

P = int(input("Digite o valor de P: "))
Q = int(input("Digite o valor de Q: "))

aux_p: int = P
digits: int = 0

while aux_p != 0:
    aux_p //= 10
    digits += 1

compare: bool = True
aux_q: int = Q

while compare:
    sub_numbers = aux_q % (10 ** digits)
    if sub_numbers == P:
        compare = False

    aux_q //= 10

    if aux_q == 0:
        compare = False

if sub_numbers == P:
    print(f"{P} é subnumero de {Q}")
else:
    print(f"{P} não é subnumero de {Q}")
