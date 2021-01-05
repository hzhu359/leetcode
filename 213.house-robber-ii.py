#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for idx in range(2, len(nums)):
            dp[idx] = max(nums[idx] + dp[idx - 2], dp[idx - 1])
        
        print(dp)

        idx = len(dp) - 1
        target = dp[idx]

        while idx > 0:
            if dp[idx] == target and dp[idx - 1] != target:
                target = dp[idx] - nums[idx]
                idx -= 1
            else:
                idx -= 1
        
        didUseOne = True if dp[idx] == target else False
        print(didUseOne)
        print(idx)
        print(target)
        
        if not didUseOne:
            return dp[len(dp) - 1]

        newnums = nums[1:]
        newdp = [0] * len(newnums)

        newdp[0] = newnums[0]
        newdp[1] = max(newnums[0], newnums[1])

        for idx in range(2, len(newnums)):
            newdp[idx] = max(newnums[idx] + newdp[idx - 2], newdp[idx - 1])
        
        return max(newdp[len(newdp) - 1], dp[len(dp) - 2])


# @lc code=end

