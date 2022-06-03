class Solution:
    def longestCommonPrefix(self, strs: list):
        s = ''
        if len(strs) == 0:
            return s

        for index,c in enumerate(strs[0]):
            for j in strs:
                if len(j) <= index:
                    return s
                
                if  j[index] != c:
                    return s
            s+=c
        return s
    
    
x = Solution()

print(x.longestCommonPrefix(['ali','bal','alfle']))