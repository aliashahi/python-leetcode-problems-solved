from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    
    def createLinkList(self,n):
        if n== 0:
            return ListNode(0)
        nl = None
        while int(n) > 0:
            nl = ListNode(n%10,nl)
            n = int(n/10)
        return nl
    
    def reverse(self,l3):
        nl = ListNode(l3.val)
        l3 = l3.next        
        while l3:
            nl = ListNode(l3.val,nl)
            l3 = l3.next
        return nl
        
    def addTwoNumbers(self, l1, l2):
        l1_num = 0
        l2_num = 0
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        
        while l1:
            l1_num*=10
            l1_num+= l1.val
            l1 = l1.next
        while l2:
            l2_num*=10
            l2_num+= l2.val
            l2 = l2.next
        
        l3  = self.createLinkList(l1_num + l2_num)
        nl = ListNode(l3.val)
        l3 = l3.next
                
        while l3:
            nl = ListNode(l3.val,nl)
            l3 = l3.next
        return nl

x = Solution()
# print(x.addTwoNumbers(ListNode(0),ListNode(0)).val)
def makeLinkList(l):
    if len(l)==0 : 
        return ListNode(0)
    x = l.pop(0)
    nl = ListNode(x)    
    nl2 = nl 
    while len(l)> 0:
        x = l.pop(0)
        nl.next = ListNode(x)
        nl = nl.next
    return nl2

print(x.addTwoNumbers(makeLinkList(
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]),makeLinkList([5,6,4])))