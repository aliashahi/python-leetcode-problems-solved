# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def _x(self, root: TreeNode ,c = 1):
        if not root.left and not root.right:
            return c
        x=[]
        if root.left:
           x.append(self._x(root.left,c+1))
        if root.right:
           x.append(self._x(root.right,c+1))
        return min(x) 
        
    def minDepth(self, root: TreeNode):
        if not root:
            return 0
        
        return self._x(root)
        