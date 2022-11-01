class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # citations.sort()
        # n, i = len(citations),1
        # while i<=n:
        #     if citations[n-i]<i:
        #         break
        #     i+=1
        # return i-1
        citations.sort(reverse=True)    
        for index,citation in enumerate(citations):
            if index>=citation:
                return index
        return len(citations)
