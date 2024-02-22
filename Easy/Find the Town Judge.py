# 997. Find the Town Judge
# https://leetcode.com/problems/find-the-town-judge/description/

from typing import List
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        inDegrees = [0] * (N + 1)
        outDegrees = [0] * (N + 1)

        for trustor, trustee in trust:
            outDegrees[trustor] += 1
            inDegrees[trustee] += 1

        for person in range(1, N + 1):
            if inDegrees[person] == N - 1 and outDegrees[person] == 0:
                return person
        return -1