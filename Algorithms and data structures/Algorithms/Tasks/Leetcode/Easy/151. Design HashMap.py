class MyHashMap:

    def __init__(self):
        self.size = 1000  # Number of buckets in the hashmap
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key, value):
        bucket_idx = key % self.size
        bucket = self.buckets[bucket_idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing key
                return
        bucket.append((key, value))  # Add new key-value pair

    def get(self, key):
        bucket_idx = key % self.size
        bucket = self.buckets[bucket_idx]
        for k, v in bucket:
            if k == key:
                return v
        return -1  # Key not found

    def remove(self, key):
        bucket_idx = key % self.size
        bucket = self.buckets[bucket_idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]  # Remove the key-value pair
                return


myHashMap = MyHashMap()
myHashMap.put(1, 1)
myHashMap.put(2, 2)
print(myHashMap.get(1))  # Output: 1
print(myHashMap.get(3))  # Output: -1
myHashMap.put(2, 1)
print(myHashMap.get(2))  # Output: 1
myHashMap.remove(2)
print(myHashMap.get(2))  # Output: -1
