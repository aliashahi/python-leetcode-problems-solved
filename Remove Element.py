class Solution:
    def removeElement(self, nums: list, val: int):
        s = []
        for index,i in enumerate(nums):
            if i != val:
                s.append(i)
                nums[len(s)-1] = i
            
        return len(s)
        