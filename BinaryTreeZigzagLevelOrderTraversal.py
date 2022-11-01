# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        q = deque()
        q.append(root)
        # q2 = []
        # level = []
        l = 1
        result = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if l % 2 == 0:
                result.append(level[::-1])
            else:
                result.append(level)
            l += 1
        return result
        #         while q1 or q2:
        #             while q1:
        #                 node = q1.pop()
        #                 level.append(node.val)
        #                 if node.left:
        #                     q2.append(node.left)
        #                 if node.right:
        #                     q2.append(node.right)
        #             if level:
        #                 result.append(level)
        #             level = []

        #             while q2:
        #                 node = q2.pop()
        #                 level.append(node.val)
        #                 if node.right:
        #                     q1.append(node.right)
        #                 if node.left:
        #                     q1.append(node.left)
        #             if level:
        #                 result.append(level)
        #             level =[]
        return result