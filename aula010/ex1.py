"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
usuário o valor do saque e depois informar quantas notas de cada valor
serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na
máquina.
	Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
	notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

	Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece
	três notas de 100, uma nota de 50, quatro notas de 10,
	uma nota de 5 e quatro notas de 1.
// %
"""

amount = int(input("Digite o valor que deseja sacar R$ "))

if 10 <= amount <= 600:
    hundred_cell = amount // 100
    amount %= 100

    fifty_cell = amount // 50
    amount %= 50

    ten_cell = amount // 10
    amount %= 10
    print(amount)
    five_cell = amount // 5
    amount %= 5

    one_cell = amount

    if hundred_cell > 0:
        print(f"{hundred_cell} notas de cem")
    if fifty_cell:
        print(f"{fifty_cell} notas de cinquenta")
    if ten_cell:
        print(f"{ten_cell} notas de dez")
    if five_cell:
        print(f"{five_cell} notas de cinco")
    if one_cell:
        print(f"{one_cell} notas de um")
else:
    print("Valor não pode ser sacado")
