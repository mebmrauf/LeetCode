# 1945. Sum of Digits of String After Convert
# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        string = ''
        for letter in s:
            string += str(ord(letter) - ord('a') + 1)
        
        for i in range(k):
            sum = 0
            for j in string:
                sum += int(j)
            string = str(sum)
        
        return int(string)