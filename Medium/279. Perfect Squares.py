# 279. Perfect Squares
# https://leetcode.com/problems/perfect-squares/description/

class Solution:
    def numSquares(self, n: int) -> int:
        # Create a list to store the minimum number of perfect square numbers for each value from 0 to n
        dp = [float('inf')] * (n + 1)
        
        # Initialize the base case
        dp[0], dp[1] = 0, 1
        
        # Iterate through each value from 1 to n
        for i in range(2, n + 1):
            # Iterate through perfect squares less than or equal to i
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1) #minimum value, remainder
                j += 1
        
        # The result is stored at the last index of dp
        return dp[n]