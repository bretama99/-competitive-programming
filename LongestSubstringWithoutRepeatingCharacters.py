class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLen = 0
        d = {}
        for end in range(len(s)):
            if s[end] in d:
                start = max(start,d[s[end]]+1)
            maxLen = max(maxLen,end-start+1)
            d[s[end]] = end
        return maxLen
        
