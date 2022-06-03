class Solution:
    def isPalindrome(self, x: int):
        s = str(x)
        for i in range(len(s)):
            if s[i] !=s[len(s)-i-1] :
                return False
        return True
        ...


x = Solution()
print(x.isPalindrome(121))
print(x.isPalindrome(122))
print(x.isPalindrome(0))
print(x.isPalindrome(2333))