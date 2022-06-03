class Solution:
    def isValid(self, s: str):
        stack = []
        for i in range(len(s)):
            if s[i] == '[' or s[i]=='(' or s[i]=='{':
                stack.append(s[i])
                continue;
            if len(stack) == 0:
                return False;
            c = stack.pop()
            if s[i]==']' and c != '[':
                return False
            if s[i]==')' and c != '(':
                return False
            if s[i]=='}' and c != '{':
                return False
        
        return len(stack) == 0

x = Solution()
print(x.isValid('[][][][][]'))
print(x.isValid('()'))
print(x.isValid("()[]{}"))