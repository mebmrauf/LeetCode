# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii

from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        finalList = []
        stack = [(0, 0, [])]
        
        while stack:
            currentSum, startIndex, targetList = stack.pop()
            if currentSum == target:
                finalList.append(targetList)
                continue
            
            for i in range(startIndex, len(candidates)):
                if i > startIndex and candidates[i] == candidates[i - 1]:
                    continue

                newSum = currentSum + candidates[i]
                if newSum > target:
                    break
                
                stack.append((newSum, i + 1, targetList + [candidates[i]]))
        
        return finalList