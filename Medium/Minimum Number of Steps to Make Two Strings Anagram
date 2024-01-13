# 1347. Minimum Number of Steps to Make Two Strings Anagram
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram

from collections import Counter # No need to import in leetcode

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum((Counter(s) - Counter(t)).values())

#OR

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dicS, dicT, count, i = {}, {}, 0, 0
        while i < len(s):
            if s[i] not in dicS:
                dicS[s[i]] = 1
            else:
                dicS[s[i]] += 1
            if t[i] not in dicT:
                dicT[t[i]] = 1
            else:
                dicT[t[i]] += 1
        
            i+=1

        for key, value in dicS.items():
            if key in dicT.keys():
                count += abs(value - dicT[key])
            else:
                count += value
        
        for key, value in dicT.items():
            if key not in dicS.keys():
                count += value
    
        return count//2