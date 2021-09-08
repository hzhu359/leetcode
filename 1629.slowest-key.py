#
# @lc app=leetcode id=1629 lang=python3
#
# [1629] Slowest Key
#

# @lc code=start
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        n = len(releaseTimes)
        ret = keysPressed[0]
        mmax = releaseTimes[0]

        for i in range(1, n):
            curr = releaseTimes[i] - releaseTimes[i - 1]
            if curr == mmax and ord(keysPressed[i]) > ord(ret) or curr > mmax:
                mmax = curr
                ret = keysPressed[i]

        return ret


# @lc code=end
