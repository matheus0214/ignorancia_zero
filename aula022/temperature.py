""" Temperatures """

NUM = int(input("Digite o número de temperaturas: "))

lesser = greater = float(input("Informe a temperature 1: "))

total: int = 0

for i in range(2, NUM + 1):
    temp = float(input(f"Informe a temperature {i}: "))

    if temp > greater:
        greater = temp

    if lesser < temp:
        lesser = temp

    total += temp

print(f"A maio temperatura {greater:6.2f}\nMenor {lesser:6.2f}\nMédia {total/NUM:6.2f}")
