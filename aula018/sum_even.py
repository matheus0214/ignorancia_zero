""" Sum even """

N = int(input("Digite o número de sequências: "))

for i in range(N):
    print(f"Sequência {i+1}")
    num = int(input("Digite um número da sequência: "))
    total: int = 0

    while num != 0:
        if num % 2 == 0:
            total += num

        num = int(input("Digite um número da sequência: "))

    print(f"A soma da sequência {i+1} é {total}")
