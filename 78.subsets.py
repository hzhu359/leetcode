#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        n = len(nums)
        def dfs(curr, idx):
            ret.append(curr)
            if not idx < n:
                return
            for i in range(idx, n):
                dfs(curr + [nums[i]], i + 1)
        dfs([], 0)
        return ret

# @lc code=end

