# LINKED LIST - Medium

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return []
        res = ListNode(0, head)
        delete = res

        for _ in range(n):
            head = head.next
        
        while head:
            head = head.next
            delete = delete.next
        
        delete.next = delete.next.next
        return res.next
