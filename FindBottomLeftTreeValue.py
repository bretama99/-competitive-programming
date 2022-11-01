# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        d = defaultdict(list)
        def dfs(root, level):  
            if not root:
                return
            d[level].append(root.val)
            dfs(root.right,level+1)
            dfs(root.left,level+1)
        dfs(root, 0)
        return list(d.values())[-1][-1]
        # q = deque([root])
        # while q:
        #     node = q.popleft()
        #     if node.right:
        #         q.append(node.right)
        #     if node.left:
        #         q.append(node.left)
        # return node.val
        
