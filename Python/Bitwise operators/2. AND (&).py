# Идет побитовое сравнение 0b101 и 0b100. В результате получаем 0b100

flags = 5
mask = 4
print(bin(flags))  # 0b101
print(bin(mask))   # 0b100

result = flags & mask
print(result)      # 4
