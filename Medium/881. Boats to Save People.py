# 881. Boats to Save People
# https://leetcode.com/problems/boats-to-save-people/

from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if min(people) > limit:
            return 0
        if (len(people) == 1 and people[0] <= limit) or \
        (len(people) == 2 and people[0] + people[1] <= limit):
            return 1

        people.sort()
        i, j = 0, len(people) - 1
        boats = 0
        
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            boats += 1
        
        return boats