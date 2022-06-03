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
    
    def generate(self, numRows: int):
        if numRows == 1:
            return [[1]]
        res = [[1]]
        for _ in range(numRows-1):
            x = res.pop()
            res.append(x)
            res.append(self.getNextRow(x))
        return res           

x = Solution()
x.generate(3)