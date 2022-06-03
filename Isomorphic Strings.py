class Solution:
    def _replaceWithCode(self,s:str):
        d = '''1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?\\ `~"'''
        l = [] # ['a','1']
        i = 0
        for c in range(len(s)):
            x=None
            for j in l:
                if j[0] == s[c]:
                    x = j
                    break
            if not x:
                x = [s[c],d[i]]
                l.append(x)
                i+=1
            s = s[:c]+ x[1] + s[c+1:]
        return s
            
                
    def isIsomorphic(self, s: str, t: str):
        return self._replaceWithCode(s) == self._replaceWithCode(t)
    

x = Solution()

print(x.isIsomorphic('add','egg'))
print(x.isIsomorphic('add','egg'))