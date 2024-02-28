# 513. Find Bottom Left Tree Value
# https://leetcode.com/problems/find-bottom-left-tree-value/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import deque
from typing import Optional
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            levelSize = len(queue)
            leftmost = None
            
            for i in range(levelSize):
                node = queue.popleft()
                if i == 0:
                    leftmost = node.val
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return leftmost