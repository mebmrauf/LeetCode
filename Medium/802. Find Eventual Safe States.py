# 802. Find Eventual Safe States
# https://leetcode.com/problems/find-eventual-safe-states/

from typing import List

# DFS
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        leng = len(graph)
        status = [0] * leng # 0: unvisited, 1: visiting, 2: safe
        
        def isSafe(node):
            if status[node] > 0:
                return status[node] == 2
            
            status[node] = 1
            
            for neighbor in graph[node]:
                if status[neighbor] == 1 or not isSafe(neighbor):  
                    return False
            
            status[node] = 2  # Mark node as safe
            return True
        
        result = []
        for i in range(leng):
            if isSafe(i):
                result.append(i)
        
        return result
    
# Topological Sorting
from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        leng = len(graph)
        reverseGraph = [[] for _ in range(leng)]
        outdegree = [0] * leng
        
        for node, neighbors in enumerate(graph):
            outdegree[node] = len(neighbors)
            for neighbor in neighbors:
                reverseGraph[neighbor].append(node)
        
        queue = deque()
        for i in range(leng):
            if outdegree[i] == 0:  # Terminal nodes
                queue.append(i)
        
        safeNodes = []
        
        while queue:
            current = queue.popleft()
            safeNodes.append(current)
            for neighbor in reverseGraph[current]:
                outdegree[neighbor] -= 1
                if outdegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return sorted(safeNodes)