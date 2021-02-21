#
# @lc app=leetcode id=1335 lang=python3
#
# [1335] Minimum Difficulty of a Job Schedule
#

# @lc code=start
import math
import pprint
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        '''
        subproblems?
        
        F(i, d) = min cost of ending on job i at day d
        F(i, 0) = 0
        F(0, d) = 0
        F(i, d) = inf if d < i (want to kick out this result)
        '''

        n = len(jobDifficulty)

        print(n, d)

        if d > n:
            return -1

        '''
        creating a max table
        mt[i][j] returns the maximum value of the range a_i, a_i+1, ..., a_j
            from the list of jobs
        '''
        max_table = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i > j:
                    max_table[i][j] = math.inf
                elif i == j:
                    max_table[i][j] = jobDifficulty[j]
                else:
                    max_table[i][j] = max(max_table[i][j-1], jobDifficulty[j])

        # pprint.pprint(max_table)

        dp = [[0 for _ in range(n + 1)] for _ in range(d + 1)]
        dp[1] = ([0] + max_table[0]).copy()

        for i in range(2, d + 1):
            for j in range(1, n + 1):

                if j < i:
                    dp[i][j] = math.inf
                else:
                    minVal = math.inf

                    for k in range(i - 1, j):
                        res = dp[i - 1][k] + max_table[k][j - 1]
                        # print(i, j, k, dp[i-1][k], max_table[k][j-1],res)
                        minVal = min(minVal, res)
                    
                    dp[i][j] = minVal

        # print(dp)

        return dp[d][n]
        
# @lc code=end

