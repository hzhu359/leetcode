#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:

        '''
        n = len(height)
        peak = max(height)
        ret = 0

        for y in range(1, peak + 1):
            last = None
            # acc = 0
            for x in range(n):
                if height[x] >= y:
                    if not last is None:
                        span = x - last - 1
                        ret += span
                    last = x
        
        return ret
        '''

        # two pointer approach - built on the min(maxL, maxR) - height rule
        # uses the bottleneck value (i.e. checks the lowest max first)
        # s.t. we only need to rely on left OR right

        n = len(height)
        left = 0
        right = n - 1

        maxleft = 0
        maxright = 0

        ret = 0

        while left <= right:
            if maxleft < maxright:
                # left boundary is minimum
                curr = height[left]
                ret += maxleft - curr if maxleft - curr > 0 else 0
                maxleft = max(maxleft, curr)
                left += 1
            else:
                curr = height[right]
                ret += maxright - curr if maxright - curr > 0 else 0
                maxright = max(maxright, curr)
                right -= 1
        
        return ret








        
# @lc code=end

