class Solution:
    def lengthOfLastWord(self, s: str):
        while '  ' in s: 
            s = s.replace('  ',' ').strip()
        
        return len(s.strip().split(' ').pop())
    

x = Solution()
print(x.lengthOfLastWord("luffy is still joyboy"))
print(x.lengthOfLastWord("   fly me   to   the moon  "))