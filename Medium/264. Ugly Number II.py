# 264. Ugly Number II
# https://leetcode.com/problems/ugly-number-ii

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNums = [1]
        n2, n3, n5 = 0, 0, 0
        for i in range(1, n):
            nextUglyNum = min(uglyNums[n2]*2, uglyNums[n3]*3, uglyNums[n5]*5)
            uglyNums.append(nextUglyNum)
            if nextUglyNum == uglyNums[n2]*2:
                n2 += 1
            if nextUglyNum == uglyNums[n3]*3:
                n3 += 1
            if nextUglyNum == uglyNums[n5]*5:
                n5 += 1
        return uglyNums[n-1]