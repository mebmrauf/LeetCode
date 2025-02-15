# 2698. Find the Punishment Number of an Integer
# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        def validPartition(index, current, target, num):
            if index == len(num) and current == target:
                return True

            for j in range(index, len(num)):
                part = int(num[index:j+1])
                if validPartition(j + 1, current + part, target, num):
                    return True
            return False

        result = 0
        for i in range(1, n + 1):
            square = i * i
            if validPartition(0, 0 , i, str(square)):
                result += square
        return result