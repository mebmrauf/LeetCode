# 129. Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, currentSum):
            if not node:
                return 0
            currentSum = currentSum * 10 + node.val
            if not node.left and not node.right:
                return currentSum
            return dfs(node.left, currentSum) + dfs(node.right, currentSum)
        
        return dfs(root, 0)