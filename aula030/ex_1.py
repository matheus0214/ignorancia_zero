"""
Faça um programa que leia um número indeterminado de valores,
correspondentes a notas, encerrando a entrada de dados quando
for informado um valor igual a -1 (que não deve ser armazenado).
Após esta entrada de dados, faça:
a.	Mostre a quantidade de valores que foram lidos;
b.	Exiba todos os valores na ordem em que foram informados
c.	Exiba todos os valores na ordem inversa à que foram informados
d.	Calcule e mostre a soma dos valores;
e.	Calcule e mostre a média dos valores;
f.	Calcule e mostre a quantidade de valores acima da média calculada;
g.	Calcule e mostre a quantidade de valores abaixo de sete;
h.	Encerre o programa com uma mensagem;
"""


num = int(input("Informe um número: "))

NUMBERS = []
while num != -1:
    NUMBERS.append(num)

    num = int(input("Informe um número: "))

print(f"Quantidade de valores lidos: {len(NUMBERS)}")
print(NUMBERS)
print(NUMBERS[::-1])

total: int = sum(NUMBERS)
median: int = 0

median = total / len(NUMBERS)
print(f"Soma dos valores {total}")

greather_than_median: int = 0
lesser_than_seven: int = 0
for i in NUMBERS:
    if i > median:
        greather_than_median += 1

    if i < 7:
        lesser_than_seven += 1

print(f"Quantidade de número acima da média {greather_than_median}")
print(f"Quantidade de número abaixo de 7: {lesser_than_seven}")
