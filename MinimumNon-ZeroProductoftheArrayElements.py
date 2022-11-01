class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10**9 + 7
        final = 2**p-1
        secondFinal = final-1
        middle = secondFinal//2
        ans = (final*(pow(secondFinal,middle,MOD)))%MOD
        return ans
        
