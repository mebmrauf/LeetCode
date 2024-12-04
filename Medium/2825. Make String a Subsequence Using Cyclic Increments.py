# 2825. Make String a Subsequence Using Cyclic Increments
# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0
        n, m = len(str1), len(str2)

        while i < n and j < m:
            char1, char2 = str1[i], str2[j]
            
            asci = ord(char1) + 1
            if asci == 123: asci = 97

            if char1 == char2 or chr(asci) == char2:
                j += 1
            i += 1
        return j == m