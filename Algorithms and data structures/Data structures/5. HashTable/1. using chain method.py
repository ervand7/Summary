from typing import List, Hashable, Any


class Node:
    def __init__(self, key: Hashable, value: Any):
        self.key = key
        self.value = value
        self.next: Node = None

    def __repr__(self):
        return f"{self.key}: {self.value}"


class HashTable:
    def __init__(self, initial_size=10):
        self.size = initial_size
        self.table: List = [None] * initial_size
        self.count = 0  # Number of key-value pairs in the table
        self.threshold = 0.7  # Load factor threshold for resizing

    def insert(self, key, value):
        index = self._get_index(key, self.size)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            current.next = Node(key, value)

        self.count += 1
        if self.count / self.size > self.threshold:
            self._resize()

    def search(self, key):
        index = self._get_index(key, self.size)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self._get_index(key, self.size)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                self.count -= 1
                return
            prev, current = current, current.next

    def display(self):
        for i in range(self.size):
            print(f"Bucket {i}:", end=" ")
            current = self.table[i]
            while current:
                print(f"({current.key}: {current.value})", end=" ")
                current = current.next
            print()

    @staticmethod
    def _get_index(key: Hashable, size: int):
        return hash(key) % size

    def _resize(self):
        new_size = self.size * 2
        new_table: List = [None] * new_size

        for bucket in self.table:
            current = bucket
            while current:
                index = self._get_index(current.key, new_size)
                if new_table[index] is None:
                    new_table[index] = Node(current.key, current.value)
                else:
                    new_node = Node(current.key, current.value)
                    new_node.next = new_table[index]
                    new_table[index] = new_node
                current = current.next

        self.table = new_table
        self.size = new_size


# Example Usage:
hash_table = HashTable()

hash_table.insert("1", "1")
hash_table.insert("2", "2")
hash_table.insert("3", "3")
hash_table.insert("4", "4")
hash_table.insert("5", "5")
hash_table.insert("6", "6")
hash_table.insert("7", "7")
hash_table.insert("8", "8")
hash_table.insert("9", "9")
hash_table.insert("10", "10")
hash_table.insert("11", "11")
hash_table.insert("city", "New York")
hash_table.insert("name", "Ivan")
hash_table.insert("name", "Ivan")
hash_table.insert("name", "Ivan")
hash_table.insert("name", "Ivan")
hash_table.insert("name", "Vasya")


hash_table.display()

print("\nSearch 'name':", hash_table.search("name"))
print("Search 'gender':", hash_table.search("gender"))

hash_table.delete("2")
hash_table.display()

# Bucket 0: (4: 4)
# Bucket 1:
# Bucket 2: (3: 3)
# Bucket 3:
# Bucket 4:
# Bucket 5:
# Bucket 6: (6: 6)
# Bucket 7: (7: 7) (name: Vasya) (name: Ivan)
# Bucket 8: (2: 2) (9: 9)
# Bucket 9: (10: 10)
# Bucket 10: (5: 5)
# Bucket 11:
# Bucket 12:
# Bucket 13: (8: 8)
# Bucket 14: (city: New York)
# Bucket 15:
# Bucket 16:
# Bucket 17: (1: 1) (11: 11)
# Bucket 18:
# Bucket 19:

# Search 'name': Vasya
# Search 'gender': None

# Bucket 0: (4: 4)
# Bucket 1:
# Bucket 2: (3: 3)
# Bucket 3:
# Bucket 4:
# Bucket 5:
# Bucket 6: (6: 6)
# Bucket 7: (7: 7) (name: Vasya) (name: Ivan)
# Bucket 8: (9: 9)
# Bucket 9: (10: 10)
# Bucket 10: (5: 5)
# Bucket 11:
# Bucket 12:
# Bucket 13: (8: 8)
# Bucket 14: (city: New York)
# Bucket 15:
# Bucket 16:
# Bucket 17: (1: 1) (11: 11)
# Bucket 18:
# Bucket 19: