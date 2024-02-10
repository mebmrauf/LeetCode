# 647. Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/description/

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        # dp[i][j] is True if s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]

        # All individual characters are palindromes
        for i in range(n):
            dp[i][i] = True
            count += 1

        # Check palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1

        # Check palindromes of length 3 or more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1

        return count