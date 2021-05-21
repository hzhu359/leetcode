#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = grid[0][0]

        def getPadded(i, j):
            if i < 0 or j < 0:
                return float('inf')
            return dp[i][j]



        for i in range(n):
            for j in range(m):
                if i == j == 0:
                    continue
                dp[i][j] = \
                    grid[i][j] \
                    + min(
                        getPadded(i - 1, j),
                        getPadded(i, j - 1))
        
        return dp[n - 1][m - 1]



# @lc code=end

