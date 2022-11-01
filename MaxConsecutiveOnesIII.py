class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroCount = start = maxCount = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount +=1
            while zeroCount > k:
                if nums[start]==0:
                    zeroCount -=1
                start +=1
            maxCount = max(maxCount,i-start+1)
        return maxCount
     
        
