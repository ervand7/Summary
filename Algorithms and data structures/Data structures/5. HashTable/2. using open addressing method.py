class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                # Key already exists, update the value
                self.values[index] = value
                return

            # Linear probing for collision resolution
            index = (index + 1) % self.size

        # Insert the key and value
        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                # Key found, return the corresponding value
                return self.values[index]

            # Linear probing for collision resolution
            index = (index + 1) % self.size

        # Key not found
        return None


# Example usage:
hash_table = HashTable(size=10)

hash_table.insert("apple", 5)
hash_table.insert("apple", 5)
hash_table.insert("orange", 8)

print(hash_table.get("apple"))  # Output: 5
print(hash_table.get("orange"))  # Output: 8
print(hash_table.get("banana"))  # Output: None
