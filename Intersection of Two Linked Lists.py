# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        l = []
        x = headA
        y = headB
        # flag = False
        while x and y:
            if x in l:
                return x
            l.append(x)
            if y in l:
                return y
            l.append(y)
            x = x.next
            y = y.next
        
        while x:
            if x in l:
                return x
            x = x.next
        
        while y:
            if y in l:
                return y
            y = y.next
            
        
        return None
        