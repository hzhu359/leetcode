#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
from bisect import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        """
        dp = [1]
        # dp @ i represents LIS ending at i
        ret = 1

        for idx in range(1, n):
            curr = nums[idx]
            mmax = 0
            for jdx in range(0, idx):
                if curr > nums[jdx]:
                    mmax = max(mmax, dp[jdx])
            dp.append(mmax + 1)
            ret = max(mmax + 1, ret)
        print(dp)
        return ret
        """

        # intelligently building subsequences w/ binary search

        from bisect import bisect_left

        ret = [nums[0]]
        for num in nums[1:]:
            if num > ret[-1]:
                ret += [num]
            else:
                idx = bisect_left(ret, num)
                if idx == len(ret):
                    ret.append(num)
                else:
                    ret[idx] = num

        return len(ret)


# @lc code=end
