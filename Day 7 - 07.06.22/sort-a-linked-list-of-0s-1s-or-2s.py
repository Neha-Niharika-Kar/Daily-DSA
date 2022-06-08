# LINKED LIST - Easy

# Given a linked list of 0s, 1s and 2s, sort it.
# Return Type: head of the new list formed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, data=0, next=None):
#         self.data = data
#         self.next = next
class Solution:
    def segregate(self, head):
        count = [0, 0, 0]
        ptr = head
        while ptr != None:
            count[ptr.data]+=1
            ptr = ptr.next
        i = 0
        ptr = head
        while ptr != None:
            if count[i] == 0:
                i+=1
            else:
                ptr.data = i
                count[i]-=1
                ptr = ptr.next
        return head
