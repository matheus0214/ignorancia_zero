""" Shop color """

AREA = int(input("Entre com a área a ser pintada: "))

liters = AREA // 3
if AREA % 3 > 0:
    liters += 1

can_paint = liters // 18
if liters % 18 > 0:
    can_paint += 1

print("Vocé precisara de", can_paint, "latas")
print("Vocé vai pagar R$", can_paint * 80, "latas")
