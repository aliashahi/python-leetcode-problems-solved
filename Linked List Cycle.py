# Definition for singly-linked list.
class ListNode:
    def __init__(self, x,next = None):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode):
        l = []
        x = head
        while x:
            if x in l:
                return True
            l.append(x)
            x = x.next
        return False


x = Solution()

n4 = ListNode(-4)
n3 = ListNode(0,n4)
n2 = ListNode(2,n3)
n1 = ListNode(3,n2)

n4.next = n2

print(x.hasCycle(n1))