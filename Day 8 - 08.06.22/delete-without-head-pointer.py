# LINKED LIST - Easy

# Given a pointer to a node to be deleted, delete the node. 
# Note that we don’t have a pointer to the head node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, data=0, next=None):
#         self.data = data
#         self.next = next
class Solution:
    def deleteNode(self,curr_node):
        if curr_node == None:
            return
        else:
            while curr_node.next:
                prev = curr_node
                curr_node.data = curr_node.next.data
                curr_node = curr_node.next
            prev.next = None
