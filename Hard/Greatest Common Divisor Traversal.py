# 2709. Greatest Common Divisor Traversal
# https://leetcode.com/problems/greatest-common-divisor-traversal/description/

from typing import List
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY

        n = len(nums)
        parent = [i for i in range(n)]  # Initialize Union-Find data structure
        groups = {}  # Dictionary to store groups of indices with the same prime factors

        # Group indices based on prime factors
        for i in range(n):
            for factor in range(2, int(nums[i]**0.5) + 1):
                if nums[i] % factor == 0:
                    if factor not in groups:
                        groups[factor] = i  # Create new group with first element
                    else:
                        union(i, groups[factor])  # Merge groups with the same factor
                    while nums[i] % factor == 0:  # Divide by factor until 1
                        nums[i] //= factor
            if nums[i] > 1:  # Handle remaining prime factors
                if nums[i] not in groups:
                    groups[nums[i]] = i
                else:
                    union(i, groups[nums[i]])

        # Check if all indices belong to the same connected component
        root = find(0)
        for i in range(1, n):
            if find(i) != root:
                return False  # Not connected, cannot traverse all pairs

        return True  # All indices are connected, traversing is possible