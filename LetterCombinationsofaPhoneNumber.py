class Solution:
    
    
    def x(self,d,s,index):
        if len(s) == index:
            return [s]
        l = []
        for i in d[int(s[index])]:
            l+= self.x(d,s[:index]+i+s[index+1:],index+1)
        return l

    def letterCombinations(self, digits: str):
        if len(digits) ==0:
            return []
        d = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        return self.x(d,digits,0)        

x = Solution()
print(x.letterCombinations('23'))
print(x.letterCombinations(''))
            
        
        