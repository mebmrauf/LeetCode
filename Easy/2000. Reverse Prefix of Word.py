# 2000. Reverse Prefix of Word
# https://leetcode.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if len(word) == 1 or ch not in word:
            return word
        else: 
            index = word.index(ch)
            return word[:index+1][::-1] + word[index+1:]