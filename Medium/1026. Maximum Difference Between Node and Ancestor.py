# 1026. Maximum Difference Between Node and Ancestor
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, minVal, maxVal):
            if not node:
                return maxVal - minVal
            
            minVal = min(minVal, node.val)
            maxVal = max(maxVal, node.val)

            leftDiff = dfs(node.left, minVal, maxVal)
            rightDiff = dfs(node.right, minVal, maxVal)

            return max(leftDiff, rightDiff)

        if not root:
            return 0

        return dfs(root, root.val, root.val)