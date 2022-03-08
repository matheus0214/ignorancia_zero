"""
Numa eleição existem três candidatos.
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos
de cada candidato.
"""
VOTERS = int(input("Digite o número de eleitores: "))

candiate_1: int = 0
candiate_2: int = 0
candiate_3: int = 0

for i in range(VOTERS):
    vote = int(
        input(
            "Digite o número do candidato\n"
            + "1 - Eula Anderson\n2 - Jeff Rodriguez\n3 - Henry Craig\nVote: "
        )
    )

    if vote == 1:
        candiate_1 += 1
    elif vote == 2:
        candiate_2 += 1
    elif vote == 3:
        candiate_3 += 1

print(f"\nO candiatato Eula Anderson recebeu {candiate_1}")
print(f"O candiatato Jeff Rodriguez recebeu {candiate_2}")
print(f"O candiatato Henry Craig recebeu {candiate_3}")
