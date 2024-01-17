# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1

import random

class RandomizedSet:

    def __init__(self):
        self.set = set()
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.set.add(val)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.list:
            self.set.remove(val)
            self.list.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)