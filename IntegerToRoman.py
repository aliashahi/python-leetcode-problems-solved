class Solution:
    def intToRoman(self, num: int):
        code = [
            ['I',1],
            ['IV',4],
            ['V',5],
            ['IX',9],
            ['X',10],
            ['XL',40],
            ['L',50],
            ['XC',90],
            ['C',100],
            ['CD',400],
            ['D',500],
            ['CM',900],
            ['M',1000]]
        code.reverse()
        s = ''
        while num != 0:
            for i in code:
                if i[1] <= num:
                    s+=i[0]
                    num-=i[1]
                    break;
        
        return s;
    
x = Solution()
print(x.intToRoman(3)) 
print(x.intToRoman(58)) 
print(x.intToRoman(1994)) 
                
        
        