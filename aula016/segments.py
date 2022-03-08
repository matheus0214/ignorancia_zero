""" Growing segments """
N = int(input("Digite o tamanho da sequência: "))
previous = int(input("Digite o número 1: "))

cont: int = 1
segment: int = 1
max_segment: int = 1

while cont < N:
    next_value = int(input(f"Digite o número {cont+1}: "))

    if next_value > previous:
        segment += 1
    else:
        if segment > max_segment:
            max_segment = segment
            segment = 1

    cont += 1
    previous = next_value

print("O maior segmento crescente da sequência é", maxSegment)
