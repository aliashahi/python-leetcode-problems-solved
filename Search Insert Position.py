class Solution:
    def searchInsert(self, nums: list, target: int):
        for index,i in enumerate(nums):
            if i >= target:
                return index
            
        return len(nums)
    

x = Solution()
print(x.searchInsert([1,3,5,6],2))