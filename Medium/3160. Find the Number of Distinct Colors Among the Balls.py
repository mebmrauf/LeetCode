# 3160. Find the Number of Distinct Colors Among the Balls
# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        result, ballColors, distinctColors = [], {}, {}

        for ball, color in queries:
            if ball in ballColors:
                prevColor = ballColors[ball]
                distinctColors[prevColor] -= 1
                if distinctColors[prevColor] == 0:
                    del distinctColors[prevColor]

            ballColors[ball] = color

            if color not in distinctColors:
                distinctColors[color] = 0
            distinctColors[color] += 1

            result.append(len(distinctColors))

        return result