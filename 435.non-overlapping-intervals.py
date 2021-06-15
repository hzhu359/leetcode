#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])
        ret = 0
        prev = 0
        curr = 1
        while curr < n:
            if intervals[curr][0] < intervals[prev][1]:
                ret += 1
                if intervals[curr][1] < intervals[prev][1]:
                    prev = curr
                curr += 1
            else:
                prev = curr
                curr += 1
        return ret









        




# @lc code=end

