"""
Modifique o simulador de megasena de forma que agora também seja contabilizado
quando se ganha quinas e quadras
"""

import random
from typing import List

MY: List[int] = []
MEGA = list(range(1, 61))

for _ in range(6):
    sorted_num = random.choice(MEGA)
    while True:
        if sorted_num not in MY:
            MY.append(sorted_num)
            break

n = int(input("Número de testes: "))
total: int = 0

for i in range(n):
    cont: int = 0
    GAME: List[int] = []

    winner: bool = False
    while not winner:
        GAME = []
        MEGA_SORT = MEGA.copy()
        quadra: bool = False
        quina: bool = False

        for _ in range(6):
            sorted_num = random.choice(MEGA_SORT)
            GAME.append(sorted_num)
            MEGA_SORT.remove(sorted_num)

        for j in range(len(MY)):
            if MY[i] in GAME:
                quadra += 1
                quina += 1

        if GAME == MY or quina == 5 or quadra == 4:
            winner = True

        GAME.sort()
        cont += 1

    total += cont

    print(f"Resultado to test {i} com {cont} tentativas")

print(f"Mẽdia {total/n}")
