# 1790. Check if One String Swap Can Make Strings Equal
# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        mismatch = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mismatch.append(i)
                if len(mismatch) > 2:
                    return False

        return (len(mismatch) == 2 and
                s1[mismatch[0]] == s2[mismatch[1]] and
                s1[mismatch[1]] == s2[mismatch[0]])