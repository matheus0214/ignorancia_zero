"""
Dados dois naturais m e n determinar, entre todos os pares de números naturais
(x,y) tais que x < m e y < n, um par para o qual o valor da expressão
x*y - x**2 + y seja máximo e calcular também esse máximo.
"""

M = int(input("Valor de M: "))
N = int(input("Valor de N: "))

total: int = 0
x_max: int = 0
y_max: int = 0

for x in range(M):
    for y in range(N):
        if x * y - x ** 2 + y > total:
            x_max = x
            y_max = y
            total = x * y - x ** 2 + y


print(f"O maior valor encontrado para a expressão {total} com valor de X {x} e Y {y}")
