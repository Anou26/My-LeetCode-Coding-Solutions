from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.requests.append(t)
        # Remove elements that are out of the 3000 ms range
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
