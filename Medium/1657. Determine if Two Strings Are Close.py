# 1657. Determine if Two Strings Are Close
# https://leetcode.com/problems/determine-if-two-strings-are-close

from collections import Counter # No need to import in leetcode

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): 
            return False
        else:
            if sorted(Counter(word1).values()) == sorted(Counter(word2).values()) and set(word1) == set(word2):
                return True
        return False
    
# If you want, you can skip line 8 - 10.
# Line 11 - 13 are sufficient to solve this problem.