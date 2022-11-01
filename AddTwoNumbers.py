# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return [0]
        node1 = ''
        cur1 = l1
        while cur1:
            node1+=str(cur1.val)
            cur1 = cur1.next
        node2 = ''
        cur2 = l2
        while cur2:
            node2+=str(cur2.val)
            cur2 = cur2.next
        sum_ = int(node1[::-1])+int(node2[::-1])
        cur =node = ListNode()
        for i in str(sum_)[:: -1]:
            cur.next = ListNode(int(i))
            cur = cur.next
        
        return node.next
        
