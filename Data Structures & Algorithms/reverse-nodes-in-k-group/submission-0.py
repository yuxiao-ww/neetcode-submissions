# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        count = 0

        while cur and count < k:
            cur = cur.next
            count += 1
        
        if count < k:
            return head
        
        prev, cur = None, head
        for _ in range(k):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        head.next = self.reverseKGroup(cur, k)

        return prev