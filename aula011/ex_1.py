"""
Faça um Programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.
	Observando os termos no plural a colocação do "e", da vírgula
	entre outros. Exemplo:
	326 = 3 centenas, 2 dezenas e 6 unidades
	12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301,
	101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

NUM = int(input("Entre com um número: "))

if NUM <= 1000:
    HUNDREDS = NUM // 100
    DOZENS = (NUM % 100) // 10
    UNITS = ((NUM % 100) % 10) % 10

    print(f"{NUM} = ", end="")
    if HUNDREDS:
        print(
            f"{HUNDREDS} ",
            end="",
        )
        if HUNDREDS > 1:
            print("centenas", end="")
            if DOZENS:
                print(", ", end="")
        else:
            print("centena ", end="")
            if DOZENS > 1:
                print("e ", end="")
        if DOZENS == 0:
            if UNITS:
                print("e ", end="")
    if DOZENS:
        print(f"{DOZENS} ", end="")
        if DOZENS > 1:
            print("dezenas", end="")
        else:
            print("dezena ", end="")
        if UNITS:
            print("e ", end="")
    if UNITS:
        print(f"{UNITS} ", end="")
        if UNITS > 1:
            print("unidades")
        else:
            print("unidade")
else:
    print("Número deve ser menor que 1000")
