# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1

import random # No need to import in LeetCode

class RandomizedSet:
    def __init__(self):
        self.dicT = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dicT:
            return False
        self.dicT[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dicT:
            return False
        index, lastElem = self.dicT[val], self.list[-1]
        self.list[index], self.dicT[lastElem] = lastElem, index

        self.list.pop()
        del self.dicT[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)