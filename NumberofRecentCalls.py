class RecentCounter(object):

    def __init__(self):
        self.a = deque()

    def ping(self, t):
        if len(self.a) == 0:
            self.a.append(t)
            return 1
        while t - self.a[0] > 3000:
            self.a.popleft()
            if len(self.a) == 0:
                self.a.append(t)
                break
        else:
            self.a.append(t)
        return len(self.a)

        """
        :type t: int
        :rtype: int
        """

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)