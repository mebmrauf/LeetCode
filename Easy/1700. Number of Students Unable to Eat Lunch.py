# 1700. Number of Students Unable to Eat Lunch
# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

from typing import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st1 = sum(students)
        st2 = len(students) - st1
        for sandwitch in sandwiches:
            if sandwitch == 0 and st2:
                st2 -= 1
            elif sandwitch == 1 and st1:
                st1 -= 1
            else:
                break
        return st1 + st2