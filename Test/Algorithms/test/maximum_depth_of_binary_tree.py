class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else: 
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return left+1 if left > right else right+1