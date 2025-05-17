# LINKED LIST - Medium

# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l1, l2 = [], []
        while head:
            if head.val < x:
                l1.append(head.val)
            else:
                l2.append(head.val)
            head = head.next
        
        values = l1 + l2
        res = ListNode(0)
        current = res
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return res.next
