# 2092. Find All People With Secret
# https://leetcode.com/problems/find-all-people-with-secret/description/

from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secrets = set([0, firstPerson])  # stores indices of those who shared secrets
        meetingTime = {}

        for src, dest, time in meetings:
            if time not in meetingTime:
                meetingTime[time] = defaultdict(list)
            
            meetingTime[time][src].append(dest)
            meetingTime[time][dest].append(src)

        for t in sorted(meetingTime.keys()):
            stack = deque()
            visited = set()

            for src in meetingTime[t]:
                if src in secrets and src not in visited:
                    stack.append(src)

                    while stack:
                        current_person = stack.pop()

                        if current_person not in visited:
                            visited.add(current_person)
                            secrets.add(current_person)

                            stack.extend(meetingTime[t][current_person])

        return list(secrets)