#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # subproblem: DP(i, j) = a palindrome can be made from s[i, j incl.]
        # base case:
        # DP(i, i) = 1
        # DP(i, i + 1) = 2 if same letter else 0
        # only extend from these
        # DP(i - 1, j + 1) = DP(i, j) + 2 if s[i - 1] && s[j + 1] and DP(i, j) else 0
        # do stuff diag.
        n = len(s)

        dp = [[False for _ in range(n)] for _ in range(n)]

        ret = ""

        for i in range(n - 1, 0 - 1, -1):
            for j in range(i, n):
                length = j - i + 1
                curr =  s[i] == s[j] and (length < 4 or dp[i + 1][j - 1])
                dp[i][j] = curr

                if curr and length > len(ret):
                    ret = s[i:j + 1]
        
        return ret







        
# @lc code=end

