#
# @lc app=leetcode id=256 lang=python3
#
# [256] Paint House
#

# @lc code=start
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        newRow = [0 for _ in range(3)] # [0, 0, 0]
        oldRow = None
        colSet = {0, 1, 2}

        for idx, row in enumerate(costs):
            oldRow = newRow[:]
            for jdx in range(len(row)):
                minVal = float('inf')
                for sdx in colSet - {jdx}:
                    minVal = min(minVal, oldRow[sdx])
                newRow[jdx] = minVal + costs[idx][jdx]
            print(newRow)
        return min(newRow)











# @lc code=end

