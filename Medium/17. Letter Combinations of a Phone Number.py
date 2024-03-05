# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from itertools import product # No need to import in LeetCode

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dicT = {'2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'}
        if len(digits) == 0:
            return []
        comb = [dicT[key] for key in digits]
        return [''.join(lComb) for lComb in product(*comb)]