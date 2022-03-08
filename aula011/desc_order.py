""" Desc order """

A = int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))
C = int(input("Digite o terceiro número: "))

if A >= B >= C:
    print(A, B, C)
elif A >= C >= B:
    print(A, C, B)
elif B >= A >= C:
    print(B, A, C)
elif B >= C >= A:
    print(B, C, A)
elif C >= A >= B:
    print(C, A, B)
else:
    print(C, B, A)
