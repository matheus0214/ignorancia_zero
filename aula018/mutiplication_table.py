""" Mutiplication Table """

INITIAL = int(input("Digite o começo = "))
LAST_ONE = int(input("Digite o fim = "))

print()
for i in range(INITIAL, LAST_ONE + 1):
    print(f"Para o {i}")
    for j in range(INITIAL, LAST_ONE + 1):
        print(f"{i}X{j} = {i*j}")
    print()
