""" Breaking """
import random

tests = int(input("Digite o número de testes: "))

should_change: int = 0
not_change: int = 0

for i in range(tests):
    port = random.randrange(1, 4)
    award = random.randint(1, 3)

    if port == award:
        not_change += 1
    else:
        should_change += 1

print(f"É vantajoso trocar em {should_change*100/tests:.2f}")
print(f"Não é vantajoso trocar em {not_change*100/tests:.2f}")
