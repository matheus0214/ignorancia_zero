""" Tens squared """

num: int = 1000
while num < 10000:
    aux: int = num
    LAST_TOW = aux % 100

    aux //= 100
    FIRST_TOW = aux % 100

    if (LAST_TOW + FIRST_TOW) ** 2 == num:
        print(num)

    num += 1
