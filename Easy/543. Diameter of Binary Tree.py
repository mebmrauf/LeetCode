# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.depthFirstSearch(root)
        return self.diameter

    def depthFirstSearch(self, root):
        if not root:
            return 0

        leftDepth = self.depthFirstSearch(root.left)
        rightDepth = self.depthFirstSearch(root.right)

        self.diameter = max(self.diameter, leftDepth + rightDepth)

        return 1 + max(leftDepth, rightDepth)