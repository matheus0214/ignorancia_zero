"""Class 28"""

import random
from typing import List

items: List[int] = []

for i in range(10000):
    items.append(random.randint(1, 6))

for i in range(1, 7):
    print(f"A face {i} apareceu {100*items.count(i)/10000:.2f}% vezes")
