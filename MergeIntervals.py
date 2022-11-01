class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda i:i[0])
        print(intervals)
        output = [intervals[0]]
        for start, end in intervals[1:]:
            startEnd = output[-1][1]
            if start<=startEnd:
                output[-1][1] = max(startEnd,end)

            else:
                output.append([start,end])
        return output
intervals = [[1,3],[2,6],[8,10],[15,18]]
solution = Solution()
aaa = solution.merge(intervals)
print(aaa)