# 739. Daily Temperatures\
# https://leetcode.com/problems/daily-temperatures/description/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        result = [0] * l
        stack = []

        for i in range(l):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prevIndex = stack.pop()
                result[prevIndex] = i - prevIndex

            stack.append(i)

        return result