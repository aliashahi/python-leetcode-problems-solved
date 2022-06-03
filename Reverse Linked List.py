# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode):
        x = None
        while head:
            x = ListNode(head.val,x)
            head = head.next
        return x