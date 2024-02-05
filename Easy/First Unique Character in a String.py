# 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/description/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            index = s.index(i)
            if i not in s[index+1:]:
                return index
        return -1