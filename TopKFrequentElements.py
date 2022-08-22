from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # sort = sorted(nums,key=lambda x:nums.count(x), reverse=True)
        count = []
        counter = Counter(nums)
        for i, j in counter.most_common(k):
            count.append(i)
        return count

