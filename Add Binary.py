class Solution:
    def addBinary(self, a: str, b: str):
        while len(a) < len(b):
            a = '0'+a
        while len(a) > len(b):
            b = '0'+b
        s = ''
        i = 1
        c = 0
        while i != len(a)+1:
            x = int(a[len(a) - i])+int(b[len(b)-i]) + c
            if x <= 1 :
                c = 0
                s= str(x) + s
            else :
                c = 1
                if x == 2:
                    s = '0' + s
                else :
                    s = '1' + s
            i+=1
        if c == 1:
            s = '1'+ s
        return s

x = Solution()

print(x.addBinary('111','101'))#1100