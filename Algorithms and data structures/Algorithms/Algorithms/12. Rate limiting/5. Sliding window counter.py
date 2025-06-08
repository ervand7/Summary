import time
import math


# It’s a smarter version of the **fixed window** algorithm.
#
# Instead of counting requests in a **single full window**, it looks at **two
# adjacent time windows** (e.g., the current second and the previous second)
# and does a **weighted average** based on how far we are into the current window.

# * Limit: 10 requests per second
# * You’re 0.3 seconds into the current window
# * You received:
#
#   * 4 requests in the **previous** window
#   * 3 requests in the **current** window
# * Weighted total = `0.7 × 4 + 0.3 × 3 = 3.7 + 0.9 = 4.6`
# * 4.6 < 10 → new request is **allowed**
#
# ### 🔁 Why it’s better:
#
# It avoids sharp cutoffs like in **fixed window**, and doesn’t require
# storing all timestamps like **sliding window log**.


class SlidingWindowCounter:
    def __init__(self, limit: int, window_sec: float):
        self.limit = limit
        self.window_sec = window_sec
        self.counters = {}  # key: window timestamp, value: count

    def allow(self) -> bool:
        now = time.time()
        current_window = math.floor(now / self.window_sec)
        prev_window = current_window - 1

        # Initialize counters if not present
        self.counters.setdefault(current_window, 0)
        self.counters.setdefault(prev_window, 0)

        # Calculate how far we are into the current window
        elapsed = now - (current_window * self.window_sec)
        weight = elapsed / self.window_sec

        # Weighted count
        count = (
                self.counters[prev_window] * (1 - weight) +
                self.counters[current_window]
        )

        if count < self.limit:
            self.counters[current_window] += 1
            return True  # allow
        return False  # reject


# ---- quick demo ----
rate_limiter = SlidingWindowCounter(limit=5, window_sec=1)

for i in range(10):
    print(i + 1, "Allowed" if rate_limiter.allow() else "Rejected")
    time.sleep(0.2)
