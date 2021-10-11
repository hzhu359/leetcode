#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
from collections import deque


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # why are we using dp here
        # optimal solutions are composed of optimal subproblems
        #   i.e. for a certain string and pattern, parts of the string match with parts of the pattern
        # subproblems build to larger solutions
        import re

        m = len(s)
        n = len(p)

        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        # base cases
        dp[0][0] = True

        # initialize top row
        # i.e. look for * and set true since empty can be true with wildcards
        for idx, c in enumerate(p):
            if idx == 0:
                continue
            if c == "*" and dp[0][idx - 1]:
                dp[0][idx + 1] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                ret = False

                scurr = s[i - 1]
                pcurr = p[j - 1]

                if pcurr == "*":
                    if scurr == p[j - 2] or p[j - 2] == ".":
                        # look before the rule (j - 2)
                        # or look if rule was matched right before (j - 1)
                        # or look if rule was matched with the curr rule but smaller string
                        ret = dp[i - 1][j] or dp[i][j - 1]
                    else:
                        # must extend by discarding
                        ret = dp[i][j - 2]
                elif pcurr == "." or pcurr == scurr:
                    ret = dp[i - 1][j - 1]
                dp[i][j] = ret

        print(dp)
        return dp[m][n]


# @lc code=end
