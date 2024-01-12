# 2610. Convert an Array Into a 2D Array With Conditions
# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        matrix = []

        for num in nums:
            found = False
            for row in matrix:
                if num not in row:
                    row.append(num)
                    found = True
                    break

            if not found:
                matrix.append([num])

        return matrix