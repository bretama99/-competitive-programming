from collections import Counter


class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        n=len(changed)
        if n%2:
            return []
        count = Counter(changed)
        changed.sort()
        ans = []
        for num in changed:
            if num==0 and count[num]>=2:
                count[num]-=2
                ans.append(num)
            elif num!=0 and count[num] and count[num*2]:
                count[num]-=1
                count[num*2]-=1
                ans.append(num)
        return ans if len(ans)==n//2 else []