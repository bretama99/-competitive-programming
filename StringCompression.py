class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        idx = 0
        while i<len(chars):
            j=i
            while j<len(chars) and chars[i]==chars[j]:
                j+=1
            chars[idx] = chars[i]
            idx+=1
            count=j-i
            
            if count>1:
                for c in str(count):
                    chars[idx] = c
                    idx+=1
            i=j
        return idx
        
