class MyHashSet:
    def __init__(self):
        self.size = 1000  # Choose a suitable size based on expected range of keys
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key):
        bucket_idx = key % self.size
        if key not in self.buckets[bucket_idx]:
            self.buckets[bucket_idx].append(key)

    def remove(self, key):
        bucket_idx = key % self.size
        bucket = self.buckets[bucket_idx]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key):
        bucket_idx = key % self.size
        bucket = self.buckets[bucket_idx]
        return key in bucket


myHashSet = MyHashSet()
myHashSet.add(1)
myHashSet.add(2)
print(myHashSet.contains(1))  # Output: True
print(myHashSet.contains(3))  # Output: False
myHashSet.add(2)
print(myHashSet.contains(2))  # Output: True
myHashSet.remove(2)
print(myHashSet.contains(2))  # Output: False
