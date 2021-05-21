#
# @lc app=leetcode id=1854 lang=python3
#
# [1854] Maximum Population Year
#

# @lc code=start
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        bMap = [0 for _ in range(0, 100 + 1)]
        dMap = bMap.copy()
        for (birth, death) in logs:
            bMap[birth - 1950] = bMap[birth - 1950] + 1
            dMap[death - 1950] = dMap[death - 1950] + 1
        
        maxYear = 0
        pop = 0
        maxPop = pop

        for i in range (0, 100 + 1):
            pop += (bMap[i] - dMap[i])
            if pop > maxPop:
                maxPop = pop
                maxYear = i

        return maxYear + 1950




# @lc code=end

