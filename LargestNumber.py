class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums)):
            max = i
            for j in range(i, len(nums)):
                a = str(nums[max]) + str(nums[j])
                b = str(nums[j]) + str(nums[max])
                if int(b) > int(a):
                    max = j
            nums[max], nums[i] = nums[i], nums[max]
        print(nums)
        a = ""
        for i in nums:
            a += str(i)
        if int(a[0]) == 0:
            return a[0]
        return a
aa = Solution()
nums = [3,30,34,5,9]
cc = aa.largestNumber(nums)
print(cc)