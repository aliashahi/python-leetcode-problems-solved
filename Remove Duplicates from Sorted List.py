# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode):
        x = head
        # l = ListNode(head.val)
        # x = l
        while x:
            if x.next and x.next.val == x.val:
                x.next = x.next.next 
            else :
                x = x.next
        return head