# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# https://leetcode.com/problems/climbing-stairs/solutions/4584244/solution-for-climbing-stairs-problem/

# MOST EFFICIENT ANSWER

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        previous, current = 1, 1
        for i in range(2, n+1):
            temp = current
            current = previous + current
            previous = temp
        return current

# OR

class Solution:
    def climbStairs(self, n: int) -> int:
        if 0 < n <= 2:
            return n
        totalWays = [0] * (n + 1)
        totalWays[1], totalWays[2] = 1, 2
        for i in range(3, n + 1):
            totalWays[i] = totalWays[i - 1] + totalWays[i - 2]
        return totalWays[n]