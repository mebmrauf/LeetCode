# 404. Sum of Left Leaves
# https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0

        result = 0
        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                result += root.left.val
            else:
                result += self.sumOfLeftLeaves(root.left)
        
        result += self.sumOfLeftLeaves(root.right)
        
        return result