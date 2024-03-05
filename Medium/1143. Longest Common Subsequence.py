# 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ftLen, stLen = len(text1), len(text2)
        lcSubStr = [[0] * (stLen + 1) for _ in range(ftLen + 1)]
        for i in range(ftLen):
            for j in range(stLen):
                if text1[i] == text2[j]:
                    lcSubStr[i+1][j+1] = lcSubStr[i][j] + 1
                else:
                    lcSubStr[i+1][j+1] = max(lcSubStr[i][j+1], lcSubStr[i+1][j])
        return lcSubStr[ftLen][stLen]