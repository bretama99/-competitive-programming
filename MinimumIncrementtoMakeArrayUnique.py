class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count = 0
        # ass = Counter(nums)
        nums.sort()
        prev = nums[0]
        for i in range(1,len(nums)):
            if prev >= nums[i]:
                count+=(prev+1)-nums[i]
                nums[i]=prev+1
                prev = nums[i]
            else:
                prev = nums[i]
        return count
