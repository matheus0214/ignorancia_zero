""" Fatorial """

N = int(input("Digite o valor de N: "))
fatorial: int = 1

# for i in range(2, N + 1):
#     fatorial *= i

for i in range(N, 1, -1):
    fatorial *= i

print(fatorial)
