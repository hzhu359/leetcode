#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        ret = []
        intervals.sort(key = lambda x: x[0])

        currInterval = intervals[0]
        
        for start, end in intervals:
            if start <= currInterval[1]:
                currInterval = (currInterval[0], max(currInterval[1], end))
            else:
                ret.append(currInterval)
                currInterval = (start, end)
        
        if not ret or ret[-1] != currInterval:
            ret.append(currInterval)
        
        return ret
        
        '''
        def doMerge(currR, nextR):
            return currR[1] >= nextR[0]

        intervals.sort(key=lambda x: x[0])
        print(intervals)
        ret = []
        idx = 0
        curr = None
        for idx, entry in enumerate(intervals):
            if not curr:
                curr = entry
                continue

            if doMerge(curr, entry):
                # extend
                curr[1] = max(entry[1], curr[1])
            else:
                # range is done
                ret.append(curr)
                curr = entry
        
        if curr: ret.append(curr)


        return ret
        '''


# @lc code=end

