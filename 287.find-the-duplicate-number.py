#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # def search(arr, low, high, target):
        #     while low <= high:
        #         mid = (low + high) // 2
        #         if arr[mid] == target:
        #             return True
        #         elif arr[mid] > target:
        #             high = mid - 1
        #         elif arr[mid] < target:
        #             low = mid + 1
        #     return False

        # n = len(nums)
        # """
        # i: number we're searching for in rest of array
        # j: start of inc. subarr.
        # k: end of inc. subarr.
        # """

        # for i in range(n - 1):
        #     j = i + 1
        #     while j < n:
        #         k = j
        #         while k + 1 < n and nums[k + 1] >= nums[k]:
        #             k += 1
                
        #         print("i: {}, j: {}, k:{}".format(nums[i],nums[j],nums[k]))
        #         if search(nums, j, k, nums[i]):
        #             return nums[i]
        #         j = k + 1
        
        # return -1

        """
        tortoise and hare?
        imagine a function f(x) = nums[x]
        and "construct" a linked list as f(0) -> f(f(0)) -> f(f(f(0))) -> ...
        since there's a duplicate in nums, eventually *another* thing in nums
        will take you back to an already-seen index, restarting the cycle

        that duplicate is the origin of the cycle
        """

        # phase 1
        tortoise = nums[0]
        hare = nums[nums[0]]

        while (nums[tortoise] != nums[hare]):
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
        

        
        # phase 2
        tortoise = 0
        while (nums[tortoise] != nums[hare]):
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return nums[tortoise]



# @lc code=end

