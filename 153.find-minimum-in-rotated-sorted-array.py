#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we're searching for a number greater than its right neighbor
        n = len(nums)
        if n == 1:
            return nums[0]

        low = 0
        high = n

        cutPoint = None

        if nums[low] < nums[high - 1]:
            return nums[low]

        while low < high:
            mid = (low + high - 1) // 2

            if nums[mid] > nums[(mid + 1) % n]:
                return nums[(mid + 1) % n]

            if nums[(mid - 1) % n] > nums[mid]:
                return nums[mid]

            if nums[low] < nums[mid]:
                # cut point right
                low = mid + 1
            else:
                # cut point left
                high = mid


# @lc code=end
