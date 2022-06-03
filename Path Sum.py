# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _x(self, root: TreeNode ,s,target:int):
        if not root.left and not root.right:
            return  s + root.val == target

        if root.left and self._x(root.left,s+root.val,target):
            return True
        if root.right and self._x(root.right,s+root.val,target):
            return True
        return False

    def hasPathSum(self, root: TreeNode, targetSum: int):
        if not root:
            return False
        return self._x(root,0,targetSum)
        