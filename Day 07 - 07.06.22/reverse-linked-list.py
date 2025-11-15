# LINKED LIST - Easy

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

# Using recursion
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
