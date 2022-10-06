# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return
        cur = head
        stack = []
        output = []
        i = 0
        while cur:
            output.append(0)
            if not stack or stack[-1][1]>cur.val:
                stack.append([i,cur.val])
            else:
                while stack and stack[-1][1]<cur.val:
                    output[stack[-1][0]] = cur.val
                    stack.pop()
                stack.append([i,cur.val])
            i+=1
            cur = cur.next
        return output
                
        
