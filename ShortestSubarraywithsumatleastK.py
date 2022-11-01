class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        queue = collections.deque()
        queue.append([0,0])
        summ = 0
        res = float('inf')
        
        for i, num in enumerate(nums):
            summ+=num
            while queue and summ - queue[0][1]>=k:
                res = min(res, i- queue[0][0]+1)
                queue.popleft()
                
            while queue and summ <= queue[-1][1]:
                queue.pop()
            queue.append([i+1,summ])
        if res < float('inf'):
            return res
        return -1
        
