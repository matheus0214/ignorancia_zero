"""
Escreva uma função que obtenha a multiplicação de vários números de entrada
"""


def multiply_values(*items):
    """multiply all values"""
    total: int = 1
    for i in items:
        total *= i

    return total


print(multiply_values(1, 2, 3))
