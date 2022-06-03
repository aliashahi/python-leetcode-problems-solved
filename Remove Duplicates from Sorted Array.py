class Solution:
    def removeDuplicates(self, nums: list):
        s = []
        for index,i in enumerate(nums):
            if i not in s:
                s.append(i)
                nums[len(s)-1] = i
            
        return len(s)