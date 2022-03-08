"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""

HOUR_SALARY = int(input("Digite o valor da hora R$: "))
HOURS_WORKED = int(input("Digite o número de horas trabalhadas: "))

print("Salário do mês R$", HOUR_SALARY * HOURS_WORKED)
