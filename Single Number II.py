class Solution:
    def singleNumber(self, nums: list):
        s = []
        d = []
        t = []
        for i in nums:
            if i not in t and i not in d and i not in s:
                s.append(i)
            elif i not in t and i not in d and i in s:
                s.remove(i)
                d.append(i)
            elif i not in t and i in d:
                d.remove(i)
                t.append(i)

        return s.pop()
    
x = Solution()
print(x.singleNumber([2,2,3,2]))