""" Equal segments """

N = int(input("Digite o tamanho do segmento: "))
ant = int(input("Digite o número 1: "))

cont: int = 1
segment: int = 1

while cont < N:
    next_value = int(input(f"Digite o número {cont+1}: "))
    if next_value != ant:
        segment += 1

    ant = next_value
    cont += 1

print(f"A sequência tem {segment} segmentos")
