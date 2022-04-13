"""Class 30"""
n = int(input("Digite o número de elementos da lista: "))

ITEMS = []
AUX = []

for i in range(n):
    element = int(input(f"Digite o elemento {i+1} de {n}: "))
    ITEMS.append(element)
    AUX.append(element)

for ele in AUX:
    show = ITEMS.count(ele)
    for i in range(show - 1):
        ITEMS.remove(ele)

print(ITEMS)
