#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
from functools import reduce
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        coins.sort()
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for idx in range(1, amount + 1):
            dpVal = float('inf')
            for coin in coins:
                if coin <= idx:
                    dp[idx] = min(dp[idx], 1 + dp[idx - coin])

        # why is this better?
        # for coin in coins:
        #     for idx in range(coin, len(dp)):
        #         dp[idx] = min(dp[idx], 1 + dp[idx - coin])


        ret = dp[amount]
        return -1 if ret == float('inf') else ret





        



# @lc code=end

