class Solution:
    def majorityElement(self, nums: list):
        nums.sort()
        return nums[int(len(nums)/2)]
        