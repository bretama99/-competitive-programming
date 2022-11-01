# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currentSum, depth):
            if not node:
                return False
            currentSum += node.val
            # print(currentSum)
            if not node.left and not node.right:
                return currentSum == targetSum
            return dfs(node.right, currentSum, depth + 1) or dfs(node.left, currentSum, depth + 1)

        return dfs(root, 0)
