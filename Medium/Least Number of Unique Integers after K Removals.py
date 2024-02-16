# 1481. Least Number of Unique Integers after K Removals
# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/

from collections import Counter
from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = list(Counter(arr).values())
        count.sort(reverse = True)
        while len(count) and k >= count[-1]:
            k -= count.pop()
        return len(count)