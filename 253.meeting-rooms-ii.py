#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II 
#

# @lc code=start
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        choices:
        1. allocate new meeting room
        2. use a freed up meeting room

        to make this choice easier maintain the most current (latest) time slot
        in the heap that represents a room

        initialize a room with the earliest start time
        '''
        intervals.sort(key=lambda x: x[0])

        rooms = []
        rooms.append(intervals.pop(0)[1])

        for idx, interval in enumerate(intervals):
            # merge cas
            if rooms[0] <= interval[0]:
                heapq.heappushpop(rooms, interval[1])
                # heapq.heappop(rooms)
                # heapq.heappush(rooms, interval[1])
            # non-merge case
            else:
                heapq.heappush(rooms, interval[1])
        print(rooms)
        return len(rooms)
# @lc code=end



