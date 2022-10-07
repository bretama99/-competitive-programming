# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def constructMaximumTree(left=0, right=len(nums)-1):
            # base case 1
            if left > right:
                return None
            # base case 2
            if left == right:
                return TreeNode(nums[left])
            maxIndex = left
            for index in range(left, right+1):
                if nums[index] > nums[maxIndex]:
                    maxIndex = index
            root = TreeNode(nums[maxIndex])
            
            root.left = constructMaximumTree(left, maxIndex-1)
            root.right = constructMaximumTree(maxIndex+1, right)
            return root
    
        return constructMaximumTree()
        
