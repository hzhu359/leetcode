#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        merge newInterval into a corresponding interval
            can choose any because if we have two intervals to choose from to merge into,
            then after merging into either of them, we'll merge those two anyways

            so just modify the interval that has interval[0] <= newInterval[0] <= interval[1]
            if no interval fits, check the first element of the newInterval and add to
                back or front depending on min and max interval start times

        then run through and merge all intervals
        '''

        if not intervals:
            return [newInterval]

        def merge(int1, int2):
            return [ min(int1[0], int2[0]), max(int1[1], int2[1]) ]
        
        def check(int1, int2):
            if int1[1] >= int2[0]:
                return True
            return False
        
        insertDex = -1
        didChange = False
        for idx, intvl in enumerate(intervals):
            if newInterval[0] > intvl[0]:
                insertDex = idx + 1
            if intvl[0] <= newInterval[0] <= intvl[1]:
                didChange = True
                intervals[idx] = merge(intvl, newInterval)
                break
        
        n = len(intervals)

        if not didChange:
            if insertDex == -1:
                intervals.insert(0, newInterval)
            else:
                intervals.insert(insertDex, newInterval)
        
        n = len(intervals)
        ret = []
            
        i = 0
        while i < n:
            j = i + 1
            while j < n and check(intervals[i],intervals[j]):
                intervals[i] = merge(intervals[i], intervals[j])
                j += 1
            ret.append(intervals[i])
            i = j

        return ret




# @lc code=end

