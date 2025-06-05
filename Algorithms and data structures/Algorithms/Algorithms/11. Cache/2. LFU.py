# LFU (Least Frequently Used) cache strategy means when the cache is full,
# it removes the item that has been used the fewest number of times.

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> value
        self.freq = {}  # key -> frequency
        self.time = {}  # key -> timestamp to break ties
        self.counter = 0  # global timestamp counter

    def get(self, key):
        if key not in self.cache:
            return -1
        self.freq[key] += 1
        self.counter += 1
        self.time[key] = self.counter
        return self.cache[key]

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.cache:
            self.cache[key] = value
            self.get(key)  # update frequency and time
            return

        if len(self.cache) >= self.capacity:
            # Find least frequently used key; break ties with oldest timestamp
            min_freq = min(self.freq.values())
            lfu_keys = [k for k in self.cache if self.freq[k] == min_freq]
            lfu_key = min(lfu_keys, key=lambda k: self.time[k])
            del self.cache[lfu_key]
            del self.freq[lfu_key]
            del self.time[lfu_key]

        # Add new key
        self.cache[key] = value
        self.freq[key] = 1
        self.counter += 1
        self.time[key] = self.counter


# Example usage:
lfu = LFUCache(2)
lfu.put(1, 'A')
lfu.put(2, 'B')
print(lfu.get(1))  # 'A'
lfu.put(3, 'C')  # evicts key 2 ('B'), since it was least frequently used
print(lfu.get(2))  # -1 (not found)
print(lfu.get(3))  # 'C'
