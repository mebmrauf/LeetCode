# 948. Bag of Tokens
# https://leetcode.com/problems/bag-of-tokens/

from typing import List
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score, maxScore, left, right = 0, 0, 0, len(tokens) - 1

        while left <= right:
            if power >= tokens[left]:
                power, score = power - tokens[left], score + 1
                left, maxScore = left + 1, max(maxScore, score)
            elif score > 0:
                power, score = power + tokens[right], score - 1
                right -= 1
            else:
                break

        return maxScore