""" Palindrome """

NUM = int(input("Digite um número: "))

aux: int = NUM
reverse: int = 0

while aux != 0:
    reverse = reverse * 10 + (aux % 10)
    aux //= 10

if reverse == NUM:
    print(f"{NUM} é palíndromo")
else:
    print(f"{NUM} não é palíndromo")
