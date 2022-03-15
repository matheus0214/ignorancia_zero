""" Round """

num = float(input("Digite um número: "))

if num != int(num):
    decimal = num - int(num)
    rounded: int = int(num)

    if decimal >= 0.5:
        rounded += 1

    print(f"{num} é decimal, arredondado {rounded}")
else:
    print(f"{num} é inteiro")
