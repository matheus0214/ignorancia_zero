""" Age """

N = int(input("Digite o número de pessoas: "))

cont: int = 1
while cont <= N:
    DAY = int(input(f"Dia de nascimento {cont}: "))
    MONTH = int(input(f"Mês de nascimento {cont}: "))
    YEAR = int(input(f"Ano de nascimento {cont}: "))
    AGE = int(input(f"Digite a idade {cont}: "))

    print(f"A pessoa fara {AGE} no dia {DAY}/{MONTH}/{YEAR+AGE}")
    cont += 1
