#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        '''
        subproblem:
            1. sell on a day: you're done
            2. do nothing on a day
            you buy the minimum stock price so far, so keep track of min

        recurrence:
            maximize something
            dp[i] = max(dp[i] - min, dp[i - 1])
        '''
        if not prices: return 0
        dp = [0] * 2
        minv = prices[0]
        dpdex = 2
        while dpdex < len(prices) + 1:
            minv = min(minv, prices[dpdex - 1])
            dp.append(max(prices[dpdex - 1] - minv, dp[dpdex - 1]))
            dpdex += 1
        print([0] + prices)
        print(dp)
        return dp.pop()
        
# @lc code=end

