# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        if not head:
            return None
        cur = node = head
        while cur:
            count+=1
            cur = cur.next
        count = count//2
        counter = 0
        while node:
            if count == counter:
                return node
            else:
                node = node.next
                counter+=1
        
