class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 1
        for i in range(len(nums) - 1):
            while j<len(nums):
                if i >= j:
                    j = i + 1
                    if j == (len(nums)):
                        break
                if nums[i] == 0:
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    else:
                        j += 1
                        if j==(len(nums)):
                            break
                else:
                    break
        return nums
                        
                
