"""Class 26"""
from typing import List


items: List[int] = []

for i in range(1, 6):
    NUM = int(input(f"Digite um número {i}: "))

    items.append(NUM)

print(items)
