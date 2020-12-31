#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        row = [0] * (n + 1) 
        dp = list(map(lambda x: row[:], range(m + 1)))
        maxlen = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    # dp[i][j] = 1 + min(self.dpGet(dp, i, j, mrange, nrange))
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    maxlen = max(maxlen, dp[i][j])
        return maxlen ** 2

# @lc code=end

