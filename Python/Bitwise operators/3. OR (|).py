flags = 8
mask = 5
print(bin(flags))   # 0b1000
print(bin(mask))    # 0b0101

result = flags | mask
print(result)       # 13
print(bin(result))  # 0b1101
