""" Median """

median = float(input("Digite o valor da nota 1: "))
median += float(input("Digite o valor da nota 2: "))
median += float(input("Digite o valor da nota 3: "))

median /= 3

if median == 10:
    print("Aprovado com distinção")
elif median >= 7.0:
    print("Aprovado")
else:
    print("Reprovado")
