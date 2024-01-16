# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1

class RandomizedSet:

    def __init__(self):
        self.list = []  

    def insert(self, val: int) -> bool:
        if val not in self.list:
            self.list.append(val)
            return True
        return False   

    def remove(self, val: int) -> bool:
        if val in self.list:
            self.list.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)