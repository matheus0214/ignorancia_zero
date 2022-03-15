"""
Dados dois números inteiros positivos i e j diferentes de 0,
imprimir todos os divisores comuns de i e j.

Exemplo: i = 2 e j = 3 a saída deverá ser : 1
i = 9, j = 21 a saída deverá ser: 1, 3
"""

I = int(input("Informe o valor de I: "))
J = int(input("Informe o valor de J: "))

cont: int = I
if J > I:
    cont = J

for i in range(1, cont):
    if I % i == 0 and J % i == 0:
        print(i)
