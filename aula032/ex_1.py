"""
Reescreva o simulador da megasena de forma que agora em vez de trabalhar com
o mesmo jogo sempre, o programa seleciona aleatoriamento o jogo do teórico
jogador. Faça apenas um teste a não ser que você resolva deixar o pc ligado
o dia inteiro.
"""


import random
from typing import List

MEGA = list(range(1, 61))

tele_sena: List[int] = []
my_game: List[int] = []

cont: int = 0
while tele_sena != my_game:
    for _ in range(6):
        tele_sort = random.choice(MEGA)
        my_sort = random.choice(MEGA)

        my_game.append(my_sort)
        tele_sena.append(tele_sort)

        if tele_sort != my_sort:
            MEGA.remove(tele_sort)
    tele_sena.sort()
    my_game.sort()
    cont += 1

print(cont)
