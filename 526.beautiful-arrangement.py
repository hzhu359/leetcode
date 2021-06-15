#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#

# @lc code=start
class Solution:
    def countArrangement(self, n: int) -> int:
        '''
        memoization approach
        '''
        dp = {}

        def dfs(i, numSet: frozenset):
            if (i, numSet) in dp:
                return dp[(i, numSet)]

            if not numSet:
                return 1
            ret = 0
            for num in numSet:
                ret += 0 if not (num % i == 0 or i % num == 0) \
                    else dfs(i + 1, numSet.difference({num}))
            
            dp[(i, numSet)] = ret
            return ret
        
        return dfs(1, frozenset(i for i in range(1, n + 1)))


# @lc code=end

