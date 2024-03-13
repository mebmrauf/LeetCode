# 2485. Find the Pivot Integer
# https://leetcode.com/problems/find-the-pivot-integer/

import math
class Solution:
    def pivotInteger(self, n: int) -> int:
        pivot = math.sqrt(n*(n+1)/2)
        if pivot - math.ceil(pivot) == 0:
            return int(pivot)
        return -1