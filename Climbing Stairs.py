class Solution:
    
    def f(self,n):
        if n == 0:
            return 1
        if n <= 2:
            return n
        return self.f(n-1)*n
 
    def x(self,o,z):
        return self.f(o+z)/(self.f(o)*self.f(z))
    
    def climbStairs(self, n: int):
        o = n
        z = 0
        c = 0 
        while True:
            c+= self.x(o,z)
            if o<=1:
                break
            z+=1
            o-=2
        return int(c)

                 