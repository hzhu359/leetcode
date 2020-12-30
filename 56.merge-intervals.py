#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

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
        # while intervals:
        #     curr = intervals.pop()
        #     cont = True
        #     while cont:
        #         low = curr[0]
        #         high = curr[1]
        #         cont = False
        #         for idx, entry in enumerate(intervals):
        #             if (low <= entry[0] <= high
        #             or low <= entry[1] <= high
        #             or entry[0] <= low <= entry[1]
        #             or entry[0] <= high <= entry[1]):
        #                 cont = True
        #                 low = min(low, high, entry[0], entry[1])
        #                 high = max(low, high, entry[0], entry[1])
        #                 curr[0] = low
        #                 curr[1] = high
        #                 intervals.pop(idx)
        #     ret.append(curr)
        # return ret



# @lc code=end

