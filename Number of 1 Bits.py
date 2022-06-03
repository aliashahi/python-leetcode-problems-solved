class Solution:
    def hammingWeight(self, n: int):
        x = str(bin(n))[2:];
        
        while len(x) < 32:
            x = '0'+x
        c = 0
        for i in x:
            if i =='1':
                c+=1
        return c