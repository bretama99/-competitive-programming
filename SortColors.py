class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # for i in range(0, len(nums)):
        #     min = i
        #     for j in range(i+1, len(nums)):
        #         if nums[j] < nums[min]:
        #             min=j
        #     nums[min], nums[i] = nums[i], nums[min]
        zeros = 0
        ones = 0
        twos = 0
        for i in nums:
            if i == 0:
                zeros += 1
            elif i == 1:
                ones += 1
            else:
                twos += 1
        for i in range(0, zeros):
            nums[i] = 0
        for i in range(zeros, zeros + ones):
            nums[i] = 1
        for i in range(ones + zeros, ones + zeros + twos):
            nums[i] = 2
        return nums