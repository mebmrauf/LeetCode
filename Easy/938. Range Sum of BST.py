# 938. Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        # Initialize the sum to 0
        totalSum = 0

        # Check if the current node's value is within the range [low, high]
        if low <= root.val <= high:
            totalSum += root.val

        # Recursively explore the left and right subtrees
        totalSum += self.rangeSumBST(root.left, low, high)
        totalSum += self.rangeSumBST(root.right, low, high)

        return totalSum