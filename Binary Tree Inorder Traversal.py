# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def inorderTraversal(self, root: TreeNode):
        l = []
        if not root:
            return l
        if root.left:
            l = l+self.inorderTraversal(root.left)
        l.append(root.val)
        if root.right:
            l = l+self.inorderTraversal(root.right)
        return l
        
            
        