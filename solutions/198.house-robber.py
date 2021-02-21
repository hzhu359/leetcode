#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        subproblem:
            1. if we rob i, we can only keep i and the max from i - 2
            2. if we don't rob i, we can keep the max from i - 1
        
        recurrence:
            dp[i] = max(a[i] + dp[i - 2], dp[i - 1])
        
        base case:
            dp[0] = a[0]
            dp[1] = max(a[0], a[1])
        '''
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for idx in range(2, len(nums)):
            dp[idx] = max(nums[idx] + dp[idx - 2], dp[idx - 1])

        return dp[len(nums) - 1]

        # if not nums:
        #     return 0

        # baton1 = 0
        # # baton2 is our result
        # baton2 = nums[0]
        # for idx in range(1, len(nums)):
        #     baton1, baton2 = baton2, max(baton1 + nums[idx], baton2)
        # return baton2


# @lc code=end

