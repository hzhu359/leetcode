#
# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#

# @lc code=start
from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        def choose2(n):
            # returns n C 2
            if n <= 1:
                return 0
            return  n * (n - 1) / 2

        ret = 0
        counts = defaultdict(int)

        for x in time:
            counts[x % 60] += 1
        
        ret += choose2(counts[0])
        ret += choose2(counts[30])

        # approach 1: just iterate from non-special cases 1 -> 29

        # for i in range(1, 29 + 1):
        #     ret += counts[i] * counts[60 - i]

        # approach 2: only iterate on times that are actually in time

        mods = list(map(lambda x: x % 60, [key for key in counts.keys() if key != 'default']))
        mods.sort()
        for i in mods:
            if i > 29:
                break
            ret += counts[i] * counts[60 - i]
        
        return int(ret)
        

        
# @lc code=end

