#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    '''
    DP[i] IS THE MAXIMUM CONTIGUOUS SUBARRAY FROM x ... i,
    WHERE X IS ANY INDEX BEFORE OR AT I

    subproblem:
        continue subarray or start anew

    recurrence:
        f(i) = max(f(i - 1) + a[i], a[i])
    base case?
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        ret = float('-inf')
        baton = 0
        for num in nums:
            baton = max(baton + num, num)
            ret = max(ret, baton)
        return ret
        
# @lc code=end

