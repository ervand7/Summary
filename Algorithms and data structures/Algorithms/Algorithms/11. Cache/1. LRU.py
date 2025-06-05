# LRU (Least Recently Used) cache strategy means when the cache is full,
# it removes the item that hasn't been used for the longest time.

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> value
        self.order = []  # keep track of usage order (least to most recent)

    def get(self, key):
        if key not in self.cache:
            return -1
        # Move the accessed key to the end (most recently used)
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            # Update value and usage
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            # Evict the least recently used key
            lru = self.order.pop(0)
            del self.cache[lru]
        # Insert new key
        self.cache[key] = value
        self.order.append(key)


# Example usage
if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))  # returns 1
    lru.put(3, 3)  # evicts key 2
    print(lru.get(2))  # returns -1 (not found)
    lru.put(4, 4)  # evicts key 1
    print(lru.get(1))  # returns -1 (not found)
    print(lru.get(3))  # returns 3
    print(lru.get(4))  # returns 4
