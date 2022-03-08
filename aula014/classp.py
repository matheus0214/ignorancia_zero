""" Class 14 """

N = int(input("Digite o número de empresas: "))
M = int(input("Digite o número de meses: "))

company: int = 1

while company <= N:
    month: int = 1
    balance: int = 0

    print(f"Empresa {company}: ")
    while month <= M:
        print(f"Mês {month}: ")
        profit = int(input("Digite o ganho no mes: "))
        spent = int(input("Gasto do mês: "))
        balance = profit - spent
        month += 1
        print("")

    if balance == 0:
        print(f"A empresa {company} ficou indiferente")
    elif balance > 0:
        print(f"A empresa {company} ficou com lucro de R$ {balance}")
    else:
        print(f"A empresa {company} ficou com deficit de R$ {balance}")

    company += 1
    print("")
