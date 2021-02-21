#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        ret = 1

        for idx, num in enumerate(nums):
            maxPred = 0
            for jdx in range(0, idx):
                if nums[jdx] < num:
                    maxPred = max(maxPred, dp[jdx])
            dp[idx] = 1 + maxPred
            ret = max(ret, dp[idx])
        return ret
# @lc code=end

