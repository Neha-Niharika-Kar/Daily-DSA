# LINKED LIST - Easy

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        pos = head
        while pos.next != None:
            if pos.val == pos.next.val:
                pos.next = pos.next.next
            else:
                pos = pos.next
        return head
