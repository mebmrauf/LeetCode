# 752. Open the Lock
# https://leetcode.com/problems/open-the-lock/

from collections import deque
class Solution:
    def openLock(self, deadends, target):
        deadends = set(deadends)
        visited = set()
        queue = deque([('0000', 0)])

        while queue:
            current, moves = queue.popleft()
            if current == target:
                return moves
            if current in deadends or current in visited:
                continue
            visited.add(current)

            for i in range(4):
                for move in [-1, 1]:
                    nextCombination = current[:i] + str((int(current[i]) + move) % 10) + current[i + 1:]
                    queue.append((nextCombination, moves + 1))

        return -1