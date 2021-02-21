#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1

        for coin in coins:
            # we go coins first because if we just increase the coin we're considering
            # we have no effect on previous sums

            # if we go amount first, we stumble upon duplicate solutions

            for i in range(coin, amount + 1):
                dp[i] = dp[i] + dp[i - coin]
        
        return dp[amount]


# @lc code=end

