from collections import deque


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
        print(self.a)
        return len(self.a)

q = RecentCounter();
a = q.ping(1)
print(a)
b=q.ping(2000)
print(b)
c=q.ping(3000)
print(c)
d=q.ping(4000)
print(d)
c=q.ping(5000)
print(c)
d=q.ping(6000)
print(d)