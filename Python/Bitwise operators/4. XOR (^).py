# XOR - то же, что и OR, но дает 0 при сравнении 1 с 1.
flags = 9
mask = 1
print(bin(flags))   # 0b1001
print(bin(mask))    # 0b0001

result = flags ^ mask
print(result)       # 8
print(bin(result))  # 0b1000
