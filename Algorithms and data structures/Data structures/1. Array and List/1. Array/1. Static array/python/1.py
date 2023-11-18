class StaticArray:
    def __init__(self, elements_count):
        self.elements_count = elements_count
        self.base_array = [0] * elements_count

    def __len__(self):
        return self.elements_count

    def get(self, index):
        if 0 <= index < self.elements_count:
            return self.base_array[index]
        else:
            raise IndexError("Index out of range")

    def set(self, index, value):
        if 0 <= index < self.elements_count:
            self.base_array[index] = value
        else:
            raise IndexError("Index out of range")

    def __str__(self):
        return str(self.base_array)


if __name__ == "__main__":
    sa = StaticArray(5)
    for i in range(5):
        sa.set(i, i * 2)
    print("Static Array:", sa)
    print("Length:", len(sa))

    sa.set(1, 999)
    print(sa.get(1))
