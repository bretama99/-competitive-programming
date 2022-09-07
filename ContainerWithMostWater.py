class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        left, right = 0, (len(height)-1)
        while left < right:
            if height[left] < height[right]:
                maximum = max(maximum, height[left]*(right-left))
                left+=1
            else:
                maximum = max(maximum, height[right]*(right-left))
                right-=1
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         minimum = min(height[i],height[j])
        #         maximum=max(maximum, minimum*(j-i))
        return maximum        
