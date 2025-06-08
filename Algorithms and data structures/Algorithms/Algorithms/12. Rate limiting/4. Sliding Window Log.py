import time
from collections import deque


# It remembers **when each request happened** (timestamps).
# Before accepting a new request, it looks at the **last N seconds**
# (e.g., 1 second) and **counts how many requests** were made in that period.
#
# * If the number is **below the limit** → allow the request.
# * If the number is **at or above the limit** → reject it.
#
# It’s called **sliding** because the time window moves forward **with
# every new request**, not in fixed steps.

class SlidingWindowLog:
    def __init__(self, limit: int, window_sec: float):
        self.limit = limit
        self.window_sec = window_sec
        self.timestamps = deque()  # stores timestamps of accepted requests

    def allow(self) -> bool:
        now = time.time()

        # Remove old timestamps outside the window
        while self.timestamps and self.timestamps[0] <= now - self.window_sec:
            self.timestamps.popleft()

        if len(self.timestamps) < self.limit:
            self.timestamps.append(now)
            return True  # allow
        return False  # reject


rate_limiter = SlidingWindowLog(limit=5, window_sec=1)

for i in range(20):
    print(i + 1, "Allowed" if rate_limiter.allow() else "Rejected")
    time.sleep(0.1)
