class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n==1 and k==1:
            return "0"
        s1 = '0'
        def invert(st):
            ss=""
            for i in range(len(st)):
                if st[i] =='1':
                    ss+='0'
                elif st[i]=='0':
                    ss+='1'
            return ss
        def reverse(st):
            str1=""
            for i in range(len(st)-1,-1,-1):
                str1+=st[i]
            return str1

        prev = '0'
        cur = ""
        for i in range(1,n):
            cur=prev+'1'+reverse(invert(prev))
            prev = cur
        return cur[k-1]
        
        
