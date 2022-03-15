"""Class 28"""

from typing import List


items: List[int] = []

num = int(input("Digite um número da sequência: "))

while num != -1:
    items.append(num)

    num = int(input("Digite um número da sequência: "))

element = int(input("Digite um elemento a ser procurado: "))

appear_count: int = 0

for i, ele in enumerate(items):
    if ele == element:
        appear_count += 1

print(f"O elemento {element} parece {appear_count} vezes na sequência")
print(f"O elemento {element} parece {items.count(element)} vezes na sequência")
