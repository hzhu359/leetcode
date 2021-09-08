#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        ret = []
        memo = {}

        def cb(n):
            if n in memo:
                return memo[n]

            from math import log2, floor

            if n == 0:
                return 0
            if n == 1:
                return 1

            ret = 1 + (cb(n - 2 ** (floor(log2(n)))))
            memo[n] = ret
            return ret

        for i in range(n + 1):
            ret.append(cb(i))

        return ret
        """

        ret = []
        for i in range(n + 1):
            ret.append(bin(i).count("1"))
        return ret


# @lc code=end
