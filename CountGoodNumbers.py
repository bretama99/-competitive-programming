class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9+7
        # def power(x,y,mod):
        #     if y==0:
        #         return 1
        #     return (x*power(x,y-1,mod))%mod
        if n%2==0:
            return (pow(20,n//2,mod))%mod
        return (5*pow(20,n//2,mod))%mod
        
