#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # subproblem:
        #   treat as single number or combine with previous
        #   can be though of as building from 
        #   a spot 1 before (if a valid stndalone number)
        #   and a spot 2 before (if a valid 2-digit number)
        # recurrence:
        #   f(i) = (valid i)? : f(i - 1) : 0 +
        #          (valid i-1,i)? : f(i - 2) : 0
        if s[0] == '0':
            return 0
        dp = []
        dp.append(1) # number of ways to build the valid second char
        dp.append(1) # number of ways to build the valid first char
        # dp: [1, 1, ...]
        dpidx = 2

        singleRange = range(1, 9 + 1)
        doubleRange = range(10, 26 + 1)

        while dpidx < len(s) + 1:
            dp.append(0)
            # valid single num
            if int(s[dpidx - 1]) in singleRange:
                dp[dpidx] += dp[dpidx - 1]
            # valid double num
            if int(s[dpidx - 2 : dpidx]) in doubleRange:
                dp[dpidx] += dp[dpidx - 2]
            dpidx += 1

        return dp.pop()
# @lc code=end

