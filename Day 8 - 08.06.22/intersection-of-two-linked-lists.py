# LINKED LIST - Easy

# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
# If the two linked lists have no intersection at all, return null.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n1, n2 = headA, headB
        if n1 and n2:
            while n1 != n2:
                if n1 is None:
                    n1 = headB
                else: 
                    n1 = n1.next
                if n2 is None:
                    n2 = headA 
                else: 
                    n2 = n2.next
        return n1
