#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def twoSum(arr, target):
            occSet = set()
            for entry in arr:
                complement = target - entry
                if complement in occSet:
                    res.add((entry, complement, target * -1))
                occSet.add(entry)

        nums.sort()
        for idx, entry in enumerate(nums):
            rightSide = nums[idx + 1:]
            twoSumRes = twoSum(rightSide, -1 * entry)
        return list(res)



# @lc code=end

