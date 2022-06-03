
class Solution:
    def isPalindrome(self, s: str):
        ns = ''
        for c in s:
            if c.isalnum():
                ns = c.lower() + ns
        
        for i in range(int(len(ns)/2)):
            if ns[i]!=ns[len(ns)-i-1]:
                return False
        return True

x = Solution()
# print(x.isPalindrome("A man, a plan, a canal: Panama"))
# print(x.isPalindrome("A"))
# print(x.isPalindrome("Ab"))
print(x.isPalindrome("0p"))