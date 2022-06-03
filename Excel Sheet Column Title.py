class Solution:
    def convertToTitle(self, columnNumber: int):
        d = [["A",1],["B",2],["C",3],["D",4],["E",5],["F",6],["G",7],["H",8],["I",9],["J",10],
             ["K",11],["L",12],["M",13],["N",14],["O",15],["P",16],["Q",17],["R",18],["S",19],
             ["T",20],["U",21],["V",22],["W",23],["X",24],["Y",25],["Z",26]]
        s = ''
        while columnNumber!=0:
            x = d[columnNumber%26 - 1]
            s= x[0]+s
            columnNumber -= x[1]
            columnNumber =  int(columnNumber / 26)
        
        return s
    

x = Solution()

print(x.convertToTitle(2))
print(x.convertToTitle(26))
print(x.convertToTitle(27))
print(x.convertToTitle(28))
print(x.convertToTitle(701))