#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def dfs(i, nums):
            if not i < n:
                return set()
            dfsRet = dfs(i + 1, nums)

            #marker
            ret = []

            ret += dfsRet
            ret.append(( nums[i],  ))

            for tup in dfsRet:
                ret.append(tuple( (nums[i],) + tup))

            return ret
        
        nums.sort()
        return set(dfs(0, nums) + [tuple()])


        
# @lc code=end

