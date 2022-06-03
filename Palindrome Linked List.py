# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getLinkedNumber(self,l1):
        l = l1
        n = ''
        while l:
            n += str(l.val)
            l = l.next
        return n
    def isPalindromeInt(self, x: str):
        s = x
        for i in range(len(s)):
            if s[i] !=s[len(s)-i-1] :
                return False
        return True
    
    def isPalindrome(self, head:ListNode):
        return self.isPalindromeInt(self.getLinkedNumber(head))


x = Solution()

print(x.isPalindrome(ListNode(1,ListNode(2,ListNode(1)))))
print(x.isPalindrome(ListNode(1,ListNode(2,ListNode(2)))))
print(x.isPalindrome(ListNode(1)))
print(x.isPalindrome(ListNode(0)))
        