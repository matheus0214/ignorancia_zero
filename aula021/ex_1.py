"""
Dados x real e n natural, calcular uma aproximação para cos x através dos
n primeiros termos da seguinte série:
cos x = 1/1 - (x**2)/2! + (x**4)/4! - (x**6)/6! + ... + ((-1)**k)*(x**2k)/((2k)!)

Compare com os resultados de sua calculadora!
"""

N = int(input("Digite o valor de N: "))
X = float(input("Digite o valor de X: "))

res: int = 1
term: int = 1
for i in range(1, N + 1):
    number: int = i * 2
    term *= -(X**2) / (number * (number - 1))
    res += term

print(term)
