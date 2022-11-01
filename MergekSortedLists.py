# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not len(lists) and not lists:
            return None
        def merge(l1,l2):
            dumy = ListNode()
            cur = dumy
            while l1 and l2:
                if l1.val>l2.val:
                    cur.next = l2
                    l2 = l2.next
                else:
                    cur.next = l1
                    l1 = l1.next
                cur = cur.next
            if l1:
                cur.next = l1
            if l2:
                cur.next = l2
            return dumy.next
        
        while len(lists)>1:
            mergedList = []
            for i in range(0, len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None
                mergedList.append(merge(l1,l2))
            lists = mergedList
        return lists[0]
        
