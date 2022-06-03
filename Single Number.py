class Solution:
    def singleNumber(self, nums: list):
        s = []
        d = []
        for i in nums:
            if i not in s:
                s.append(i)
            elif i in d:
                continue
            elif i in s:
                s.remove(i)
                d.append(i)    
        
        return s.pop()
    

x = Solution()
print(x.singleNumber([4,1,2,1,2]))