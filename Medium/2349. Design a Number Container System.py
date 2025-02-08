# 2349. Design a Number Container System
# https://leetcode.com/problems/design-a-number-container-system/

import heapq

class NumberContainers:
    def __init__(self):
        self.idxNum = {}
        self.index = {}

    def change(self, index: int, number: int) -> None:
        self.idxNum[index] = number
        if number not in self.index:
            self.index[number] = []
        heapq.heappush(self.index[number], index)

    def find(self, number: int) -> int:
        if number not in self.index:
            return -1
        while self.index[number]:
            i = self.index[number][0]
            if self.idxNum[i] == number:
                return i
            heapq.heappop(self.index[number])
        return -1  


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)