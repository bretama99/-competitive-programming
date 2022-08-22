from collections import Counter

class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left, res = len(arr), 0
        for element, count in Counter(arr).most_common():
            left -= count
            res += 1
            if left <= len(arr) // 2:
                return res