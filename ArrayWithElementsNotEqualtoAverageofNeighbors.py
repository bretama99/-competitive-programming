class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        arranged = []
        left = 0
        right = len(nums) - 1
        while len(arranged) != len(nums):
            arranged.append(nums[left])
            left += 1
            if left <= right:
                arranged.append(nums[right])
                right -= 1
        return arranged;
