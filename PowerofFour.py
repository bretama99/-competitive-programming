class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n<=0:
            return False
        
        x,i=1,1
        while x<=n:
            if x==n:
                return True
            x=4**i
            i+=1
        return False
        
        
