# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int):
        while head and head.val == val:
            head = head.next
        x = head
        while x:
            if x.next and x.next.val == val:
                x.next = x.next.next
            else :
                x = x.next
            
        return head