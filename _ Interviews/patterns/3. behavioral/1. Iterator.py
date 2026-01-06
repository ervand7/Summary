# Iterator — traverse a collection without exposing its structure
# ❓ The idea
# Access elements one by one without knowing how the collection is implemented.

class Counter:
    def __init__(self, limit: int):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


# Usage
for x in Counter(3):
    print(x)
