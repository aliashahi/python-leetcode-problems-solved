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
    
    def isSafeOrder(self,s):
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                count+=1
            if s[i] == ')':
                count-=1
            if count < 0:
                return False
        return True
                
    
    def x(self,s,n):
        if len(s) == n:
            if self.isValid(s):
                return [s]
            else :
                return []
        x1 = []
        if self.isSafeOrder(s +')'):
            x1 = self.x(s+')',n)
        return x1 + self.x(s + '(', n)
        
            
    def generateParenthesis(self, n: int):
        return self.x('',2* n)
        
x = Solution()
print(x.generateParenthesis(3))