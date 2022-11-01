# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        q, res = deque([(root, 1)]), 0
        while q:
            node, parentVal = q.popleft()
            for child in node.left, node.right:
                if child:
                    if parentVal % 2 == 0:
                        res += child.val
                    q.append((child, node.val))
        return res
        # self.ans = 0
#         def dfs(root, parent,gparent):
#             if not root:
#                 return 0
#             a = 0
#             if gparent and gparent.val%2==0:
#                 a +=root.val
#             print(root.val)
#             return a+dfs(root.left,root,parent) +dfs(root.right,root,parent)

#         return dfs(root,None,None)
# second solution
#         def dfs(root):
#             if not root:
#                 return 0
#             if root.val%2==0:
#                 if root.left:
#                     if root.left.left:
#                         self.ans +=root.left.left.val
#                     if root.left.right:
#                         self.ans +=root.left.right.val
#                 if root.right:
#                     if root.right.left:
#                         self.ans +=root.right.left.val
#                     if root.right.right:
#                         self.ans += root.right.right.val
#             dfs(root.left)
#             dfs(root.right)

#         dfs(root)
#         return self.ans
