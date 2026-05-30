# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            if not l1 or not l2:
                return l1 if l1 else l2
            
            dummyhead = ListNode(0)
            cur = dummyhead

            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            
            cur.next = l1 if l1 else l2
            return dummyhead.next
        
        if not lists:
            return None
        
        res = None
        for l in lists:
            res = merge(res, l)
        
        return res