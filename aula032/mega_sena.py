"""Mega sena"""

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

    while GAME != MY:
        GAME = []
        MEGA_SORT = MEGA.copy()

        for _ in range(6):
            sorted_num = random.choice(MEGA_SORT)
            GAME.append(sorted_num)
            MEGA_SORT.remove(sorted_num)

        GAME.sort()
        cont += 1

    total += cont

    print(f"Resultado to test {i} com {cont} tentativas")

print(f"Mẽdia {total/n}")
