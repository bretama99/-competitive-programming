class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = {}
        for task in tasks:
            if task not in freq:
                freq[task]=1
            else:
                freq[task]+=1
        freq = [value for key, value in freq.items()]
        max_val = max(freq)
        count = freq.count(max_val)
        return max(len(tasks), ((max_val-1)*(n+1)+count))
            
                
                    
            
        
