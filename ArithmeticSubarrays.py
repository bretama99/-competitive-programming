class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        ans = [True] * len(l)

        for i in range(len(l)):
            arthemethic = sorted(nums[l[i]:r[i] + 1])
            for j in range(2, len(arthemethic)):
                if arthemethic[j] - arthemethic[j - 1] != arthemethic[j - 1] - arthemethic[j - 2]:
                    ans[i] = False
                    break
        return ans