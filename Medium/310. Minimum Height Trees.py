# 310. Minimum Height Trees
# https://leetcode.com/problems/minimum-height-trees/

from collections import defaultdict
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adjacencyList = defaultdict(set)
        for u, v in edges:
            adjacencyList[u].add(v)
            adjacencyList[v].add(u)

        leaves = [node for node in adjacencyList if len(adjacencyList[node]) == 1]

        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for leaf in leaves:
                neighbor = adjacencyList[leaf].pop()
                adjacencyList[neighbor].remove(leaf)
                if len(adjacencyList[neighbor]) == 1:
                    newLeaves.append(neighbor)
            leaves = newLeaves

        return leaves