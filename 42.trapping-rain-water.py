#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        @ a position the maximum water stored is
        the max of the max barrier to the left
        and the max of the max barrier to the right

        pointWater = max(fromLeft, fromRight) - curr

        if we know that leftMax or the rightMax is less, we don't need to know the value of the other
        
        thus update from the outside in whenever one is less
        '''

        n = len(height)

        i = 0
        j = n - 1

        maxLeft = 0
        maxRight = 0

        ret = 0

        while i <= j:
            print(ret)
            if maxLeft < maxRight:
                curr = height[i]
                ret += max(0, maxLeft - curr)
                maxLeft = max(maxLeft, curr)
                i += 1
            else:
                curr = height[j]
                ret += max(0, maxRight - curr)
                maxRight = max(maxRight, curr)
                j -= 1
        
        return ret






        
# @lc code=end

