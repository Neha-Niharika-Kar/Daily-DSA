# LINKED LIST - Easy

# Given two numbers represented by linked lists, multiply these two linked lists. 
# The output could be large, take modulo 10^9+7.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, data=0, next=None):
#         self.data = data
#         self.next = next
MOD = 10**9+7
class Solution: 
    def multiplyTwoList(head1, head2):
        a1, a2 = [], []
        node1 = head1
        node2 = head2
        while node1 != None or node2 != None:
            if node1 != None:
                a1.append(node1.data)
                node1 = node1.next
            if node2 != None:
                a2.append(node2.data)
                node2 = node2.next
        s1 = [str(i) for i in a1]
        s2 = [str(i) for i in a2]
        num1 = int("".join(s1))
        num2 = int("".join(s2))
        return (num1 * num2)%MOD
