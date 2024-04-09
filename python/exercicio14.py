area: int = 100
litros: float = (area / 6) * 1.1

# lata -> 18
# galao -> 3.6

latas = 35 // 18
resto = 35 % 18

print(latas, (resto // 3.6) + 1)