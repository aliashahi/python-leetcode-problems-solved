class Solution:
    def hasReundent(self,s):
        c = []
        for i in s:
            if i in c:
                return True
            c.append(i)
        return False

    def lengthOfLongestSubstring(self, s: str):
        maxL  = 0;
        for i in range(len(s)):
            for j in range(i+maxL,len(s)):
                print(i,j,s[j],s[i:j])
                if not s[j] in s[i:j]:
                    x = len(s[i:j+1])
                    
                    if x>maxL:
                        maxL = x
                else :
                    break
        return maxL

x = Solution()
# print(x.lengthOfLongestSubstring(' '))
# print(x.lengthOfLongestSubstring('abcabcb'))
# print(x.lengthOfLongestSubstring('adakwflfkw;kqw;flk'))
print(x.lengthOfLongestSubstring('pwwkew'))