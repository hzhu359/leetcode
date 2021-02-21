#
# @lc app=leetcode id=1646 lang=python3
#
# [1646] Get Maximum in Generated Array
#

# @lc code=start
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        arr = [0] * (n + 1)
        arr[0] = 0
        arr[1] = 1

        ret = 1

        for idx in range(2, n + 1):
            even = (idx % 2 == 0)
            quot = idx // 2

            if even:
                arr[idx] = arr[quot]
            else:
                arr[idx] = arr[quot] + arr[quot + 1]
            
            ret = max(ret, arr[idx])
        
        return ret


# @lc code=end

