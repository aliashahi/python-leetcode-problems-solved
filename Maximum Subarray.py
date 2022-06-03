from xmlrpc.client import MAXINT


class Solution:
    def maxSubArray(self, nums: list):
        max_so_far = -MAXINT - 1
        max_ending_here = 0
      
        for i in range(len(nums)):
            max_ending_here = max_ending_here + nums[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0  
        return max_so_far
    
x = Solution()
# print(x.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
# print(x.maxSubArray([1]))
# print(x.maxSubArray([5,4,-1,7,8]))
print(x.maxSubArray([-2,8,-3,-5,10,1,-5,4]))#6