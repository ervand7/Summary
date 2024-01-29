def find_complement(num: int) -> int:
    power = 1
    while power <= num:
        power *= 2
        
    return power - num - 1
