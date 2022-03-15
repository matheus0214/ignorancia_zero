""" Right triangle """

side_1 = int(input("Digite o primeiro lado: "))
side_2 = int(input("Digite o segundo lado: "))
side_3 = int(input("Digite o terceiro lado: "))

if (
    side_1 ** 2 + side_2 ** 2 == side_3 ** 2
    or side_1 ** 2 + side_3 ** 2 == side_2 ** 2
    or side_2 ** 2 + side_3 ** 2 == side_1 ** 2
):
    print("O triângulo é retângulo")
