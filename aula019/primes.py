""" Prime numbers """

N = int(input("Digite o valor de N: "))

div: int = 0
for i in range(1, N + 1):
    prime: bool = True
    j: int = 2

    while j < i and prime:
        div += 1
        if i % j == 0:
            prime = False

        j += 1

    if prime:
        print(i)

print(f"Número de divisões {div}")
