# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isMirror(leftroot, rightroot):
            if leftroot and rightroot:
                return leftroot.val == rightroot.val
                and isMirror(leftroot.left, rightroot.right)
                and isMirror(leftroot.right, rightroot.left)

        return leftroot == rightroot

    return isMirror(root.left, root.right)


