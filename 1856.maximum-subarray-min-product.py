#
# @lc app=leetcode id=1856 lang=python3
#
# [1856] Maximum Subarray Min-Product
#

# @lc code=start
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:


        



        # n = len(nums)
        # dp = [[None for _ in range(n)] for _ in range(n)]
        # ret = 0

        # for i in range(n):
        #     for j in range(i, n):
        #         # format of tuples: (sum, min, dp)
        #         if (i == j):
        #             num = nums[i]
        #             newDP = num ** 2
        #             dp[i][j] = (num, num, newDP)
        #             ret = max(ret, newDP)
        #         else:
        #             old = dp[i][j-1]
        #             newJ = nums[j]
        #             newSum = old[0] + newJ
        #             newMin = min(old[1], newJ)
        #             newDP = newSum * newMin
        #             dp[i][j] = (newSum, newMin, newDP)
        #             ret = max(ret, newDP)
        # return ret % (10**9 + 7)

        # ret = 0
        # n = len(nums)
        # dp = [[0 for _ in range(n)] for _ in range(2)]

        # dp[1][0] = nums[0]
        # dp[0][0] = dp[1][0] ** 2

        # for idx in range(1, n):
        #     # extend
        #     oldMin = dp[1][idx - 1]
        #     oldSum = dp[0][idx - 1]

        #     contMin = min(oldMin, nums[idx])
        #     contSum = ((oldSum // oldMin) + nums[idx]) * contMin

        #     # anew
        #     newMin = nums[idx]
        #     newSum = newMin ** 2

        #     if newSum > contSum:
        #         dp[0][idx] = newSum
        #         dp[1][idx] = newMin
        #     else:
        #         dp[0][idx] = contSum
        #         dp[1][idx] = contMin
        #     ret = max(ret, dp[0][idx])
        # return ret







# @lc code=end

