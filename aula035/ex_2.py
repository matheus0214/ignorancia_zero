"""
Escreva uma função que obtenha o maior número de uma sequência de números
"""


def greater(*items):
    """multiply all values"""
    total: int = 0
    for i in items:
        if i > total:
            total = i

    return total


print(greater(1, 2, 3))
