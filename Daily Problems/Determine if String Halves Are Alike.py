# 1704. Determine if String Halves Are Alike (Easy)
# https://leetcode.com/problems/determine-if-string-halves-are-alike

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = int(len(s)/2)
        vowels = "aeiouAEIOU" 
        a, b, c1, c2 = s[:l], s[l:], 0, 0
        for i in a:
            if i in vowels:
                c1+=1
        for j in b:
            if j in vowels:
                c2+=1
        return c1 == c2