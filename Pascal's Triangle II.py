class Solution:
    def getNextRow(self,c:list):
        l = []
        for i in range(len(c)):
            if i == 0:
                l.append(c[i])
            if i == len(c)-1:
                l.append(c[i])
                continue
            l.append(c[i]+c[i+1])
        return l
    
    def getRow(self, rowIndex: int):
        if rowIndex == 0:
            return [1]
        res = [1]
        for _ in range(rowIndex):
            res = self.getNextRow(res)
        return res 

x = Solution()
print(x.getRow(0))
print(x.getRow(1))
print(x.getRow(2))
print(x.getRow(3))