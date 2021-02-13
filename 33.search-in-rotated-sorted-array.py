#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def minSearch(low, high):
            print("{} {}".format(low, high))
            mid = (low + high) // 2
            midItem = nums[mid]

            if midItem > nums[mid + 1]:
                return mid + 1

            if midItem >= nums[low]:
                return minSearch(mid + 1, high)
            else:
                return minSearch(low, mid - 1)

        def bSearch(low, high):
            print("{} {}".format(low, high))
            mid = (low + high) // 2
            midItem = nums[mid]
            if high < low:
                return -1

            if (midItem == target):
                return mid
            elif (midItem > target):
                return bSearch(low, (mid - 1))
            else:
                return bSearch((mid + 1), high)

        if nums[0] <= nums[len(nums) - 1]:
            return bSearch(0, len(nums) - 1)

        pivotDex = minSearch(0, len(nums) - 1)
        zeroElem = nums[0]

        if target >= zeroElem:
            return bSearch(0, pivotDex - 1)
        else:
            return bSearch(pivotDex, len(nums) - 1)
        
# @lc code=end

