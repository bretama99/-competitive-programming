class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque()
        # cache = set()
        q.append(start)
        while q:
            size = len(q)
            for _ in range(size):
                index = q.popleft()
                if arr[index] == 0:
                    return True
                left, right = index - arr[index], index + arr[index]
                arr[index] = -1
                if 0 <= left < len(arr) and arr[left] >= 0:
                    q.append(left)
                if 0 <= right < len(arr) and arr[right] >= 0:
                    q.append(right)

            # for x in ((index+arr[index]),(index-arr[index])):
            #     if x>=0 and x<len(arr) and x not in cache:
            #         q.append(x)
            #         cache.add(x)
        return False
