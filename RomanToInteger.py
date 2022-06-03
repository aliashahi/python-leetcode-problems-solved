class Solution:
    def romanToInt(self, s: str):
        n = 0
        code = [['I',1],['V',5],['X',10],['L',50],['C',100],['D',500],['M',1000]]
        
        exceptions = [
            ['IV','IIII'],
            ['IX','VIIII'],
            ['XL','XXXX'],
            ['XC','LXXXX'],
            ['CD','CCCC'],
            ['CM','DCCCC'],
        ]
        
        for i in exceptions:
            if i[0] in s:
                s = s.replace(i[0],i[1])

        for i in s:
            for j in code:
                if j[0] == i:
                    n+= j[1]
        return n
    

x = Solution()
print(x.romanToInt('III'))
print(x.romanToInt('LVIII'))
print(x.romanToInt('MCMXCIV'))