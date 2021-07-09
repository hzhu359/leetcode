#
# @lc app=leetcode id=1134 lang=python3
#
# [1134] Armstrong Number
#

# @lc code=start
class Solution:
    def isArmstrong(self, n: int) -> bool:
        k = len(str(n))
        for c in str(n):
            n -= int(c) ** k
        return n == 0
        
# @lc code=end

