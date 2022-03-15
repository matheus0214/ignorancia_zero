""" Sum total """

n = int(input("Digite o valor de N: "))

total: float = 0.0

for i in range(1, n + 1):
    total += i / (n - 1 + 1)

print(f"A soma vale {total}")
