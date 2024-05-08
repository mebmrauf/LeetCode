# 506. Relative Ranks
# https://leetcode.com/problems/relative-ranks/

from typing import List
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scores = sorted(score, reverse=True)
        ranks = {}
        for i, s in enumerate(scores):
            if i == 0:
                ranks[s] = "Gold Medal"
            elif i == 1:
                ranks[s] = "Silver Medal"
            elif i == 2:
                ranks[s] = "Bronze Medal"
            else:
                ranks[s] = str(i + 1)
        return [ranks[score[i]] for i in range(len(score))]