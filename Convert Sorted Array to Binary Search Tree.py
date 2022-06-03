# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list):
        if len(nums) == 0:
            return None
        x= int(len(nums)/2)
        r = TreeNode(nums[x])
        r.left = self.sortedArrayToBST(nums[:x])
        r.right = self.sortedArrayToBST(nums[x+1:])
        return r