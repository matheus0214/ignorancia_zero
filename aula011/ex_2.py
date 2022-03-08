"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

NUM1 = int(input("Entre com o primeiro número: "))
NUM2 = int(input("Entre com o segundo número: "))
NUM3 = int(input("Entre com o terceiro número: "))

if NUM1 <= NUM2 <= NUM3:
    print(NUM1, NUM3)
elif NUM1 <= NUM3 <= NUM2:
    print(NUM1, NUM2)
elif NUM2 <= NUM1 <= NUM3:
    print(NUM2, NUM3)
elif NUM2 <= NUM3 <= NUM1:
    print(NUM2, NUM1)
elif NUM3 <= NUM1 <= NUM2:
    print(NUM3, NUM2)
else:
    print(NUM3, NUM1)
