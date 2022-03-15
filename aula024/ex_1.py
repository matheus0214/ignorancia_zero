"""
Escreva um programa para simular o jogo das portas. Faça um programa que tenha
a saída como a seguinte:

Olá, bem-vindo ao nosso programa! Vamos ver se você vai ganhar um carro ou não!
Escolha uma porta: 3
Você escolheu a porta 3, mas
eu lhe informo que na porta 2 há um bode.
Deseja trocar de porta (1 - Sim/ 0 - Não): 1
Ganhou um carro!
"""
import random

print("Olá, bem-vindo ao nosso programa! Vamos ver se você vai ganhar um carro ou não!")

PORT = int(input("Escolha uma porta: "))

AWARD = random.randint(1, 3)
no_award: int = 0

if PORT == AWARD:
    print("Ganhou um carro!")
else:
    for i in range(1, 4):
        if not i == AWARD:
            no_award = i

    print(f"Você escolheu a porta {PORT}, mas")
    print(f"eu lhe informo que na porta {no_award} há um bode.")

    CHANGE = int(input("Deseja trocar de porta (1 - Sim/ 0 - Não): "))

    if CHANGE == 1:
        for i in range(1, 4):
            if not i == AWARD or not i == no_award:
                PORT = i

    if PORT == AWARD:
        print("Ganhou um carro!")
