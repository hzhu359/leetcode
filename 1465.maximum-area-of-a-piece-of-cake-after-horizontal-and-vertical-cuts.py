#
# @lc app=leetcode id=1465 lang=python3
#
# [1465] Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
#

# @lc code=start
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        def maxCut(length: int, cuts: list):
            """
            takes some length of string (say)
            cuts it at all cuts specified in cuts
            and returns the longest segment
            """
            cuts.sort()
            maxim = 0
            last = 0
            for c in cuts:
                maxim = max(maxim, c - last)
                last = c
            maxim = max(maxim, length - last)
            return maxim

        return (maxCut(h, horizontalCuts) * maxCut(w, verticalCuts)) % (10**9 + 7)
# @lc code=end

