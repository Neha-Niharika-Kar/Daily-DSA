# LINKED LIST - Easy

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        result = None
        while head:
            if not result and head.val != val:
                result = head
            if head.next and head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return result
