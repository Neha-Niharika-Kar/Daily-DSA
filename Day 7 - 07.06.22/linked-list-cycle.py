# LINKED LIST - Easy

# Given head, the head of a linked list, return true if there is a cycle in the linked list. Otherwise, return false.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        slow = fast = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
