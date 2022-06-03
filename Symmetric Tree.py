# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode):
        if not p and not q:
            return True
        if p and not q:
            return False
        if q and not p:
            return False
        
        if p.val!=q.val:
            return False
        
        return self.isSameTree(p.right,q.left) and self.isSameTree(p.left,q.right) 
    
    def isSymmetric(self, root: TreeNode):
        if not root:
            return True
        if not root.left and not root.right:
            return True
        
        return self.isSameTree(root.left,root.right)
        