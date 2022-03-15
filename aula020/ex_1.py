"""
Tendo como dados de entrada a altura e o sexo de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7 (h = altura)
Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.
"""

HEIGHT = float(input("Entre com a altura do usuário: "))
OP = float(input("Entre com o sexo do usuário: "))

if OP == 1:
    print(f"Peso ideal {(72.7*HEIGHT)-58}")
else:
    print(f"Peso ideal {(62.1*HEIGHT)-44.7}")
