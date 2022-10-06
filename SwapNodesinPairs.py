# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = slow=fast = head
        while fast:
            if fast.next:
                fast = fast.next
            slow.val, fast.val = fast.val,slow.val
            fast = fast.next
            slow = slow.next
            if slow:
                slow = slow.next
        return cur
        
