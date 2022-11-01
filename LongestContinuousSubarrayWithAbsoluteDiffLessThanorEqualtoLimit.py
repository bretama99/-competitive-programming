class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        decQ=collections.deque()
        incQ = collections.deque()
        ans=left=0
        for right,num in enumerate(nums):
            while decQ and decQ[-1]<num:
                decQ.pop()
            decQ.append(num)
            while incQ and incQ[-1]>num:
                incQ.pop()
            incQ.append(num)
            while decQ[0]-incQ[0]>limit:
                if decQ[0] == nums[left]:
                    decQ.popleft()
                if incQ[0]==nums[left]:
                    incQ.popleft()
                left+=1
            ans = max(ans,right-left+1)
        return ans
