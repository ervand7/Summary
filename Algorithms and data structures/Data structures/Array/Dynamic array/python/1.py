# A dynamic array data structure in Python can be implemented using a
# list. Python lists are dynamic arrays that automatically resize when needed.
# Here's an example of how to create a dynamic array and perform common operations:

class DynamicArray:
    def __init__(self):
        self.base_array = []
        self.capacity = 0
        self.elements_count = 0

    def __len__(self):
        return self.elements_count

    def append(self, element):
        if self.elements_count == self.capacity:
            self._resize()
        self.base_array[self.elements_count] = element
        self.elements_count += 1

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

    def insert(self, index, value):
        if index < 0 or index >= self.elements_count:
            raise IndexError("Index out of range")
        if self.elements_count == len(self.base_array):
            self._resize()
        for i in range(self.elements_count, index, -1):
            self.base_array[i] = self.base_array[i - 1]
        self.base_array[index] = value
        self.elements_count += 1

    def remove(self, value):
        index = 0
        while index < self.elements_count:
            if self.base_array[index] == value:
                break
            index += 1
        if index == self.elements_count:
            raise ValueError("Value not found")
        for i in range(index, self.elements_count - 1):
            self.base_array[i] = self.base_array[i + 1]
        self.base_array[self.elements_count - 1] = None
        self.elements_count -= 1

    def _resize(self):
        self.capacity = max(1, 2 * len(self.base_array))
        new_base_array = [0] * self.capacity
        for i in range(self.elements_count):
            new_base_array[i] = self.base_array[i]
        self.base_array = new_base_array

    def __str__(self):
        return str(self.base_array[:self.elements_count])


if __name__ == "__main__":
    da = DynamicArray()
    for i in range(17):
        da.append(i)
    print("Dynamic Array:", da)
    print("Length:", len(da))
    print("Element at index 5:", da.get(9))
    da.set(2, 99)
    print("After setting index 2 to 99:", da)
    da.insert(7, 42)
    print("After inserting 42 at index 3:", da)
    da.remove(6)
    print("After removing element 6:", da)

# Dynamic Array: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# Length: 17
# Element at index 5: 9
# After setting index 2 to 99: [0, 1, 99, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# After inserting 42 at index 3: [0, 1, 99, 3, 4, 5, 6, 42, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# After removing element 6: [0, 1, 99, 3, 4, 5, 42, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
