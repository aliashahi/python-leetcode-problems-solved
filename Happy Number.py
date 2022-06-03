class Solution:
    def _doPowering(self,n):
        x = 0
        for i in str(n):
            x+= int(i)**2
        return x
    
    def isHappy(self, n: int):
        count = 0
        while n != 1:
            n = self._doPowering(n)
            count+=1
            if count > 40:
                return False
        return True