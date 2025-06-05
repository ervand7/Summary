import time


# It counts how many requests happen in a fixed time window (e.g., 1 second).
# If the number exceeds the limit, new requests are rejected until the next
# time window starts.
#
# Think of a stopwatch that resets every second.
# You allow up to 5 requests per second.
# If 5 come in fast, the 6th is blocked — until the next second starts.

class FixedWindowCounter:
    def __init__(self, limit, window_size_sec):
        self.limit = limit
        self.window_size = window_size_sec
        self.counter = 0
        self.window_start = time.time()

    def allow_request(self):
        now = time.time()
        if now - self.window_start >= self.window_size:
            self.window_start = now
            self.counter = 0  # Reset the counter

        if self.counter < self.limit:
            self.counter += 1
            return True  # allow
        else:
            return False  # reject


# Example usage:
rate_limiter = FixedWindowCounter(limit=5, window_size_sec=1)

for i in range(10):
    allowed = rate_limiter.allow_request()
    print(f"Request {i + 1}: {'Allowed' if allowed else 'Rejected'}")
    time.sleep(0.2)
