#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
from functools import reduce
from typing import Counter


class Solution:
    from collections import Counter
    from functools import reduce
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        return min(counts.get('b', 0), counts.get('a', 0), counts.get('l', 0) // 2, counts.get('o', 0) // 2, counts.get('n', 0))


        
# @lc code=end

