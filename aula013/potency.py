""" Potency """

NUM = int(input("Base: "))
EXP = int(input("Expoente: "))

cont: int = 0
product: int = 1

while cont < EXP:
    product *= NUM
    cont += 1

print(product)
