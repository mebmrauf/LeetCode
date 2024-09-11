# 2220. Minimum Bit Flips to Convert Number
# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = self.decimalTObinary(start)
        goal = self.decimalTObinary(goal)
        
        lens, leng = len(start), len(goal)
        if lens > leng:
            goal = ('0' * (lens - leng)) + goal
        elif leng > lens:
            start = ('0' * (leng - lens)) + start
        
        count = 0
        for i in range(len(start)):
            if start[i] != goal[i]:
                count += 1   
        return count

    def decimalTObinary(self, num: int) -> str:
        if num == 0:
            return '0'
        binaryNumber = ''
        while num > 0:
            binaryNumber = str(num % 2) + binaryNumber
            num = num // 2
        return binaryNumber