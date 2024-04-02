# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/

from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dicS, dicT = defaultdict(int), defaultdict(int)
        for i, (cs, ct) in enumerate(zip(s,t)):
            if dicS[cs] != dicT[ct]:
                return False
            
            dicS[cs] = i + 1
            dicT[ct] = i + 1

        return True