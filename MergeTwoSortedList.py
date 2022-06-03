# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def getNumberRepersentaiton(self,l1):
        l = l1
        x = 0;
        while l:
            x*=10
            x+=l.val
            l = l.next
        return x

    def mergeTwoLists(self, list1:ListNode, list2:ListNode):
        if not list1 or not list2:
            if not list1:
                return list2
            if not list2 :
                return list1
            
        if not list1 and not list2:
            return None
        
        x = ListNode()
        if list1.val <= list2.val:
            x = list1
            list1 = list1.next
        else :
            x = list2
            list2 = list2.next    
        
        result = ListNode(x.val)
        nl = result
        while x:
            if not list1 and list2:
                x= list2
                list2 = list2.next
            elif not list2 and list1:
                x= list1
                list1 = list1.next
                
            elif not list2 and not list1:
                break
            
            elif list1.val <= list2.val:
                x = list1
                list1 = list1.next
            else :
                x = list2
                list2 = list2.next

            nl.next = ListNode(x.val)
            nl = nl.next
        
        return result

x = Solution()

x.mergeTwoLists(ListNode(1,ListNode(2,ListNode(4)))
                          ,ListNode(1,ListNode(3,ListNode(4))))