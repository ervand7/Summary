# My solution (slow)
class RecentCounter:

    def __init__(self):
        self.data = []

    def ping(self, t: int) -> int:
        self.data.append(t)
        return len([i for i in self.data if (t - 3000) <= i <= t])


# ChatGPT solution (fast)
class RecentCounter:
    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        # Remove requests that are outside the time frame of the last 3000 milliseconds
        while self.requests[0] < t - 3000:
            self.requests.pop(0)
        return len(self.requests)
