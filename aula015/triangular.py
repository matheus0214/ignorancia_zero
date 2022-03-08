""" Triangular numbers """

TRIANGULAR = int(input("Digite um número: "))

x: int = 1

while x * (x + 1) * (x + 2) < TRIANGULAR:
    x += 1

if x * (x + 1) * (x + 2) != TRIANGULAR:
    print(f"{TRIANGULAR} não é triangular")
else:
    print(f"{TRIANGULAR} é triangular")
