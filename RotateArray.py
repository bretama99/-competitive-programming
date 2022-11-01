class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:]+nums[:-k]
        # for i in range(k):
        #     temp = nums[len(nums)-1]
        #     for j in range(len(nums)-1,0,-1):
        #         nums[j] = nums[j-1]
        #     nums[0] = temp
        return nums
