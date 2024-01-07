def reverse_bits(n: int) -> int:
    result = 0
    for i in range(32):
        bit = (n >> i) & 1  # Extract the i-th bit from n
        result = result | (bit << (31 - i))  # Set the bit in the reverse position
    return result


# Example usage
n1 = 0b00000010100101000001111010011100
n2 = 0b11111111111111111111111111111101

# Output the results
print(f"Reversed {n1}: {reverse_bits(n1)}")  # Reversed 43261596: 964176192
print(f"Reversed {n2}: {reverse_bits(n2)}")  # Reversed 4294967293: 3221225471
