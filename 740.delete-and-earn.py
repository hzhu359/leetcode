#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        hmap = dict()
        maxVal = 0
        minVal = nums[0]

        for num in nums:
            hmap[num] = hmap.setdefault(num, 0) + num
            maxVal = max(maxVal, num)
            minVal = min(minVal, num)

        dp = [0,0]

        for i in range(minVal, maxVal + 1):
            dp.append(max(dp[-1], dp[-2] + hmap.get(i, 0)))
        
        return dp[-1]




# @lc code=end

