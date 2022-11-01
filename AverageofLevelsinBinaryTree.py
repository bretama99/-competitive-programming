# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        result = []
        queue.append(root)

        while queue:
            qLen = len(queue)
            level = 0
            count = 0
            for i in range(qLen):
                node = queue.popleft()
                if node:
                    level += node.val
                    count += 1
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if level or count:
                result.append(level / count)
        return result
