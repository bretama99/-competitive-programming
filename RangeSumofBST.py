# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # arr = []
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     arr.append(root.val)
        #     dfs(root.right)
        # dfs(root)
        # i = arr.index(low)
        # j = arr.index(high)
        # return sum(arr[i:j+1])
        if not root:
            return 0
        elif root.val < low:
            return self.rangeSumBST(root.right, low,high)
        elif root.val>high:
            return self.rangeSumBST(root.left,low,high)
        else:
            return self.rangeSumBST(root.left,low,high) +root.val+self.rangeSumBST(root.right,low,high)
        
