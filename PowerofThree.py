class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n<=0:
            return False
        x,i=1,1
        
        while x<=n:
            if x==n:
                return True
            x = 3**i
            i+=1
        return False
