# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and list2:
            return list2
        if not list2 and list1:
            return list1
        if not list1 and not list2:
            return list1
        
        cur1 = list1
        cur2 = list2
        new = ListNode()
        cur = new

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
        
        if cur1:
            while cur1:
                cur.next = cur1
                cur1 = cur1.next
                cur = cur.next
        if cur2:
            while cur2:
                cur.next = cur2
                cur2 = cur2.next
                cur = cur.next
        
        return new.next