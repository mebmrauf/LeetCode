# 2402. Meeting Rooms III
# https://leetcode.com/problems/meeting-rooms-iii/description/

from heapq import heappush, heappop
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Initialize a list to keep track of the number of bookings for each room
        roomBookingsCount = [0] * n
        
        # Initialize two lists: 'availableRooms' for available rooms and 'roomsInUse' for rooms in use
        availableRooms, roomsInUse = list(range(n)), []
        
        # Sort the meetings based on their start times
        meetings.sort(key=lambda meeting: meeting[0])

        # Iterate through the sorted meetings
        for startTime, endTime in meetings:
            # Check for available rooms at the current start time
            while roomsInUse and roomsInUse[0][0] <= startTime:
                # Move rooms from 'roomsInUse' to 'availableRooms' if their end time is before or at the start time
                heappush(availableRooms, heappop(roomsInUse)[1])
            
            # Allocate a room for the current meeting
            if len(availableRooms) == 0:
                # If no available rooms, find the room with the earliest end time and update the end time of the current meeting
                endTimeOfEarliestMeeting, roomIndex = heappop(roomsInUse)
                endTime += endTimeOfEarliestMeeting - startTime
            else:
                # Allocate an available room
                roomIndex = heappop(availableRooms)
            
            # Update the booking count for the allocated room
            roomBookingsCount[roomIndex] += 1
            
            # Mark the room as in use with the updated end time
            heappush(roomsInUse, (endTime, roomIndex))

        # Find the room with the maximum number of bookings
        maxBookingIndex = 0
        for i, bookingsCount in enumerate(roomBookingsCount):
            if bookingsCount > roomBookingsCount[maxBookingIndex]:
                maxBookingIndex = i

        # Return the index of the room with the most bookings
        return maxBookingIndex