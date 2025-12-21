import time
from collections import deque


# Simple idea:
# Imagine a bucket where water (requests) is poured in randomly but leaks out at
# a fixed rate (e.g., 1 drop per second).
# If too much water is poured in too quickly and the bucket overflows — the extra
# water (requests) is discarded.
#
# So, it smooths out bursts and ensures a constant, steady rate of processing.


class LeakyBucket:
    def __init__(self, capacity, leak_rate_per_sec):
        self.capacity = capacity
        self.queue = deque()
        self.leak_rate = leak_rate_per_sec
        self.last_leak_time = time.time()

    def allow_request(self):
        now = time.time()
        elapsed = now - self.last_leak_time

        leaks = int(elapsed * self.leak_rate)
        for _ in range(min(leaks, len(self.queue))):
            self.queue.popleft()

        self.last_leak_time = now

        if len(self.queue) < self.capacity:
            self.queue.append(now)
            return True  # allow
        else:
            return False  # reject (bucket overflow)


# Example usage:
bucket = LeakyBucket(capacity=5, leak_rate_per_sec=1)

for i in range(10):
    allowed = bucket.allow_request()
    print(f"Request {i + 1}: {'Allowed' if allowed else 'Rejected'}")
    time.sleep(0.5)
