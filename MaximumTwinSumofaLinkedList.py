# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        arr=[]
        summ = 0
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        n = len(arr)
        for i in range(n//2):
            summ=max((arr[n-1-i] +arr[i]),summ) 
        return summ
        
