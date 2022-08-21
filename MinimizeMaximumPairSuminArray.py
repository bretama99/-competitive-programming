class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        i, j = 0, len(nums) - 1
        ans = nums[0] + nums[len(nums) - 1]
        while i < j:
            if nums[i] + nums[j] > ans:
                ans = nums[i] + nums[j]
            i += 1
            j -= 1

        return ans