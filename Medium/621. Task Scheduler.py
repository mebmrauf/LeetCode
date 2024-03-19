# 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/

from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        taskCounts = Counter(tasks)
        
        # Get the maximum frequency
        maxFreq = max(taskCounts.values())
        
        # Count the number of tasks with maximum frequency
        maxCount = sum(1 for count in taskCounts.values() if count == maxFreq)
        
        # Calculate the total intervals required
        totalIntervals = (maxFreq - 1) * (n + 1) + maxCount
        
        # Return the maximum of total intervals and the length of tasks
        return max(totalIntervals, len(tasks))