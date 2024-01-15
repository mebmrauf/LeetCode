# 2225. Find Players With Zero or One Losses
# https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins, losses = {}, {}

        for winner, loser in matches:
            wins[winner] = wins.get(winner, 0) + 1
            losses[loser] = losses.get(loser, 0) + 1

        winner = [player for player in wins if player not in losses]
        loser = [player for player in losses if losses[player] == 1]

        winner.sort()
        loser.sort()

        return [winner, loser]