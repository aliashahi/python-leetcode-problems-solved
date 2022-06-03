class Solution:
    def containsDuplicate(self, nums: list):
        j = 0
        for i in nums:
            if i in nums[j+1:]:
                return True
            j+=1
        return False

x = Solution()

print(x.containsDuplicate([1,2,3,1]))