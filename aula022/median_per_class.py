""" Classes """

CLASSES = int(input("Digite a quantiade de turmas: "))

total: int = 0
for i in range(1, CLASSES + 1):
    qtd = int(input(f"Digite o número de alunos da turma {i}: "))

    while qtd < 0 or qtd > 40:
        print("\nNúmero de alunos inválido.")
        qtd = int(input(f"Digite o número de alunos da turma {i}: "))

    total += qtd

print(f"A média dos alunos é {total/CLASSES:.2g} alunos por turma")
