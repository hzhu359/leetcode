#
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#

# @lc code=start
class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        from collections import defaultdict

        n = len(profit)

        prof = {}
        dp = [0]
        endTimeMap = defaultdict(list)

        latestEndTime = -1

        for i in range(n):
            sT = startTime[i]
            eT = endTime[i]

            latestEndTime = max(latestEndTime, eT)
            prof[(sT,eT)] = profit[i]
            endTimeMap[eT].append((sT, eT))
        
        for i in range(1, latestEndTime + 1):
            '''
            at each time point in the DP, we want to maximize profit
            we do this by maximizing two options:
                1. use one of the jobs ending at time i
                    in this case we must make room by clearing space from the previous optimal solution
                    i.e. delete all other jobs with endtimes greater than the new job's starttime
                2. just skip
            '''

            # if nothing ends at this time, move on
            if len(endTimeMap[i]) == 0:
                dp.append(dp[-1])
                continue

            # ADAPT TO MULTIPLE JOBS LATER
            maxNewMax = dp[-1] 
            for newJob in endTimeMap[i]:
                newMax = dp[newJob[0]] + prof[newJob]
                if newMax > maxNewMax:
                    maxNewMax = newMax

            if maxNewMax > dp[-1]:
                dp.append(maxNewMax)
            else:
                dp.append(dp[-1])

        return dp[-1]




# @lc code=end

