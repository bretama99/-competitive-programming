"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
level = 0
d = {}
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
#         def dfs(node):
#             global level,d
#             if not node:
#                 return
            
#             for c in node.children:
#                 dfs(c)
#             level+=1
            
#         dfs(root)
#         return level
        # if not root:
        #     return 0
        # queue = deque()
        # queue.append(root)
        # depth = 0
        # while queue:
        #     size = len(queue)
        #     depth+=1
        #     for _ in range(size):
        #         node= queue.popleft()
        #         print(node.children)
        #         for child  in node.children:
        #             queue.append(child)
        # return depth
        if not root:
            return 0
        if not root.children:
            return 1
        
        return 1+max([self.maxDepth(c) for c in root.children])

        
