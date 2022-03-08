"""
Dados n e uma seqüência de n números inteiros,
determinar a soma dos números pares.
"""
SEQUENCE = int(input("Quantidade da sequência: "))

cont: int = 0
total: int = 0

while cont < SEQUENCE:
    number = int(input("Digite um número: "))
    if number % 2 == 0:
        total += number
    cont += 1

print(f"A soma da sequência e {total}")
