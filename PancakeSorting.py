class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        output=[]
        for i in range(len(arr)):
            max1 = max(arr[:len(arr)-i])
            index = arr.index(max1)+1
            arr[:index] = reversed(arr[:index])
            output.append(index)
            arr[:len(arr)-i] = reversed(arr[:len(arr)-i])
            output.append(len(arr)-i)
        return output