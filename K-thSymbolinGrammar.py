class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # def reverse(st):
        #     str1=""
        #     for i in range(len(st)):
        #         if st[i]=='1':
        #             str1+='10'
        #         elif st[i]=='0':
        #             str1+='01'
        #     return str1
        # prev = '01'
        # cur = ""
        # for i in range(2,n):
        #     cur=reverse(prev)
        #     prev = cur
        # return (prev[k-1])
        
        if n==1 and k==1:
            return 0
        mid = pow(2,n-1)/2
        if k<=mid:
            return self.kthGrammar(n-1,k)
        else:
            return self.kthGrammar(n-1,k-mid) ^1
        # return bin(k - 1).count('1') & 1
#         def bitCount(n):
#             result = 0
#             while n:
#                 n &= n - 1
#                 result += 1
#             return result

#         return bitCount(k-1) % 2
