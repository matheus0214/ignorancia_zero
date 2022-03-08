"""
Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou
em galões de 4 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 4 litros;
    misturar latas e galões, de forma que o preço seja o menor.

Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias
    int()
    //
    %
    if

    110 -> 19 liters
"""
area = int(input("Informe a área a ser pintada: "))
# area += area * 0.1

liters = area // 5
if area % 5 > 0:
    liters += 1

can_tint = liters // 18
if area % 18 > 0:
    can_tint += 1

gallons_tint = liters // 4
if area % 4 > 0:
    gallons_tint += 1

BUT_CAN_TINT = 0
BUY_GALLONS_TINT = 0

if liters >= 18:
    BUT_CAN_TINT = liters // 18
    if liters % 18 > 0:
        BUY_GALLONS_TINT = (liters - (BUT_CAN_TINT * 18)) // 4
        if (liters - (BUT_CAN_TINT * 18)) % 4:
            BUY_GALLONS_TINT += 1
else:
    BUY_GALLONS_TINT = liters // 4
    if liters % 4 > 0:
        BUY_GALLONS_TINT += 1

print(f"Para pintar a área de {area} metros você precisara de {liters} litros de tinta")
print(f"Será necessário {can_tint} latas de 18 litros, R$ {can_tint*80}")
print(f"Será necessário {gallons_tint} galões de 4 litros, R$ {gallons_tint*25}")
print("\033[32m\033[4mPara realizar uma compra melhor você podera comprar\33[0m\33[0m")
if BUT_CAN_TINT > 0:
    print(f"{BUT_CAN_TINT} latas de tinta")
    if BUY_GALLONS_TINT > 0:
        print(f"{BUY_GALLONS_TINT} galões de tinta")
else:
    print(f"{BUY_GALLONS_TINT} galões de tinta")
