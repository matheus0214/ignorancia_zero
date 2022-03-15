"""
Dados n e dois números inteiros positivos i e j diferentes de 0,
imprimir em ordem crescente os n primeiros naturais que são múltiplos de i ou
de j e ou de ambos.

Exemplo: Para n = 6 , i = 2 e j = 3 a saída deverá ser : 0,2,3,4,6,8.
"""

N = int(input("Digite um número: "))
I = int(input("Digite o valor de I: "))
J = int(input("Digite o valor de J: "))


cont: int = 0
i: int = 0
while cont < N:
    if i % I == 0 or i % J == 0:
        print(i)
        cont += 1

    i += 1
