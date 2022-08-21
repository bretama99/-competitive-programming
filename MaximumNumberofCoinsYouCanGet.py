class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        ans = 0
        piles.sort(reverse=True)
        print(piles)
        i, j = 1, len(piles) - 1
        while i < j:
            ans += piles[i]
            print(piles[i])
            i += 2
            j -= 1
        return ans
