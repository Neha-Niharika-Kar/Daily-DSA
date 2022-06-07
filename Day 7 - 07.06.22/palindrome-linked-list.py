# LINKED LIST - Easy

# Given the head of a singly linked list, return true if it is a palindrome.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pos = head
        arr = []
        while pos != None:
            arr.append(pos.val)
            pos = pos.next
        if arr == arr[::-1]:
            return True
        else:
            return False
