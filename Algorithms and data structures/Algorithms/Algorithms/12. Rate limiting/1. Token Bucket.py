import time


# The Token Bucket Algorithm is a way to control how often something can
# happen — like how many requests a server accepts.
#
# Simple idea:
# Imagine a bucket that slowly fills with tokens (e.g., 1 token per second).
# Each request needs 1 token to be allowed.
# If there’s a token — the request goes through.
# If no tokens — the request is rejected or delayed.
#
# So, it allows bursts (if tokens were saved up) but still controls
# the average rate over time.

class TokenBucket:
    def __init__(self, capacity, refill_rate_per_sec):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate_per_sec
        self.last_checked = time.time()

    def allow_request(self):
        now = time.time()
        elapsed = now - self.last_checked
        self.last_checked = now

        # Refill tokens
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)

        if self.tokens >= 1:
            self.tokens -= 1
            return True  # allow
        else:
            return False  # reject


# Example usage:
bucket = TokenBucket(capacity=5, refill_rate_per_sec=1)

for i in range(50):
    allowed = bucket.allow_request()
    print(f"Request {i + 1}: {'Allowed' if allowed else 'Rejected'}")
    time.sleep(0.2)
