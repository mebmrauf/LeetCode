# 623. Add One Row to Tree
# https://leetcode.com/problems/add-one-row-to-tree/

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot

        self.dfs(root, val, depth, 1)
        return root

    def dfs(self, node, val, depth, currentDepth):
        if not node:
            return
        
        if currentDepth == depth - 1:
            leftChild = TreeNode(val)
            leftChild.left = node.left
            node.left = leftChild
            
            rightChild = TreeNode(val)
            rightChild.right = node.right
            node.right = rightChild
            
            return
        
        self.dfs(node.left, val, depth, currentDepth + 1)
        self.dfs(node.right, val, depth, currentDepth + 1)