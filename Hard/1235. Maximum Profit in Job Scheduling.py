# 1235. Maximum Profit in Job Scheduling
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)

        dp = [0] * n
        dp[0] = jobs[0][2]

        for i in range(1, n):
            # Binary search to find the latest non-overlapping job
            low, high = 0, i - 1
            while low <= high:
                mid = (low + high) // 2
                if jobs[mid][1] <= jobs[i][0]:
                    low = mid + 1
                else:
                    high = mid - 1

            # Include the current job or exclude it
            inclusive = jobs[i][2] + (dp[low - 1] if low > 0 else 0)
            exclusive = dp[i - 1]

            # Update the maximum profit at this position
            dp[i] = max(inclusive, exclusive)

        return dp[n - 1]