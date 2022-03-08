""" Factorial """

NUM = int(input("Digite um número: "))

prod: int = NUM
aux: int = NUM - 1

while aux > 1:
    prod *= aux
    aux -= 1

print(prod)
