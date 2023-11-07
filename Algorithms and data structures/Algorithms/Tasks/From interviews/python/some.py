def my_func(z: int, y: list):
    found_values = set()
    for a in y:
        if z - a in found_values:
            return True
        found_values.add(a)
    return False
