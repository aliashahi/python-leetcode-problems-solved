# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def getD(self,node,c=1):
        x = [c]
        if node.left:
            x.append(self.getD(node.left,c+1))
        if node.right:
            x.append(self.getD(node.right,c+1))
        return max(x)
    
    def maxDepth(self, root: TreeNode):
        if not root :
            return 0
        return self.getD(root)
        