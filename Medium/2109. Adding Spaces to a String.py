# 2109. Adding Spaces to a String
# https://leetcode.com/problems/adding-spaces-to-a-string/

from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        index, temp = 0, ""
        for i in spaces:
            temp += s[index:i]+" "
            index = i
        temp += s[index:]
        return temp