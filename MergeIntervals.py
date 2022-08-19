class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda i:i[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            startEnd = output[-1][1]
            if start<=startEnd:
                output[-1][1] = max(startEnd,end)
            else:
                output.append([start,end])
        return output