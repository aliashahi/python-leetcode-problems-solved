class Solution:
    def reverseBits(self, n: int):
        x = str(bin(n))[2:];
        
        while len(x) < 32:
            x = '0'+x
        s = ''
        for i in x:
            s = i+s
        return int(s,2)
        

x = Solution()        
print(x.reverseBits(964176192))