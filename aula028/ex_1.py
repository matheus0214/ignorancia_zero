"""
Uma grande emissora de televisão quer fazer uma enquete entre os seus
telespectadores para saber qual o melhor jogador após cada jogo.
Para isto, faz-se necessário o desenvolvimento de um programa, que será
utilizado pelas telefonistas, para a computação dos votos.

Sua equipe foi contratada para desenvolver este programa, utilizando a
linguagem de programação Python.
Para computar cada voto, a telefonista digitará um número, entre 1 e 23,
correspondente ao número da camisa do jogador.
Um número de jogador igual zero, indica que a votação foi encerrada.
Se um número inválido for digitado, o programa deve ignorá-lo,
voltando a pedir outro número.
Após o final da votação, o programa deverá exibir:

a.	O total de votos computados;
b.	Os números e respectivos votos de todos os jogadores que receberam votos;
c.	O percentual de votos de cada um destes jogadores;
d.	O número do jogador escolhido como o melhor jogador da partida,
        juntamente com o número de votos e o percentual de votos dados a ele.

Observe que os votos inválidos e o zero final não devem ser computados como
votos. O resultado aparece ordenado pelo número do jogador.
O programa deve fazer uso de listas.

Exemplo de execução:
>>>
Enquete: Quem foi o melhor jogador?

Informe um valor entre 1 e 23 ou 0 para sair!

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da Votação:

Foram computados 8 votos

Jogador          Votos          %
   9                4          50.0%
  10                3          37.5%
  11                1          12.5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50.0% do total de votos.
>>>
"""

from typing import List

print("Enquete: Quem foi o melhor jogador?")
print("Informe um valor entre 1 e 23 ou 0 para sair!\n")

num = int(input("Número do jogador (0=fim): "))

VOTES: List[int] = []
PARSED: List[int] = []

number_best: int = 0
votes_best: int = 0


while num != 0:
    if 1 <= num <= 23:
        VOTES.append(num)

    num = int(input("Número do jogador (0=fim): "))

for i, v in enumerate(VOTES):
    IS_INSERTED = False
    ID_INSERTED = -1

    for i_p, v_p in enumerate(PARSED):
        if v_p[0] == v:
            IS_INSERTED = True
            ID_INSERTED = i_p

    if IS_INSERTED:
        PARSED[ID_INSERTED][1] += 1
    else:
        PARSED.append([v, 1])

print(PARSED)
print("Resultado da Votação:\n")
print(f"Foram computados {len(VOTES)} votos")

print(f"Jogador {'Votos':>10} {'%':>10}")
for i, v in enumerate(PARSED):
    if v[1] > votes_best:
        votes_best = v[1]
        number_best = v[0]

    print(f"{v[0]:3}{v[1]:13}{100*v[1]/len(VOTES):13.2f}%")

print(
    f"O melhor jogador foi o número {number_best}, com {votes_best} "
    + f"votos, correspondendo a {100*votes_best/len(VOTES):.2f}% do total de votos."
)
