"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contraram para desenvolver o programa que calculará os
reajustes.

o	Faça um programa que recebe o salário de um colaborador e o
        reajuste segundo o seguinte critério, baseado no salário atual:

o	salários até R$ 280,00 (incluindo) : aumento de 20%
o	salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
o	salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
o	salários de R$ 1500,00 em diante : aumento de 5%

Após o aumento ser realizado, informe na tela:
o	o salário antes do reajuste;
o	o percentual de aumento aplicado;
o	o valor do aumento;
o	o novo salário, após o aumento.

"""

SALARY = float(input("Entra com o salário: "))

percent: int = 0
increase: int = 0

if SALARY <= 280:
    percent = 20
elif SALARY >= 280 and SALARY < 700:
    percent = 15
elif SALARY >= 700 and SALARY < 1500:
    percent = 10
else:
    percent = 5

increase = SALARY * (percent / 100)
print(
    f"Salário atual R${SALARY} aumento de {percent}% aumento de R${increase} novo salário R${SALARY+increase}"
)
