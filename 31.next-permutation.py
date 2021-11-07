#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        4 6 5 3

        4 3       5 4 3 2
          i - 1   i
        4 4       5 3 3 2



        4 4 5 3 3 2

        4 3 2 1
                ___

        find the (non-strictly) increasing from the back sequence

        swap with the lowest in this sequence greater than the lef telement

        sort
        """

        n = len(nums)
        start = 0
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        
        if i == -1:
            nums.sort()
            return
        
        leftDex = i
        i += 1

        while i < n and nums[i] > nums[leftDex]:
            i += 1
        
        i -= 1

        def swap(idx1, idx2):
            temp = nums[idx1]
            nums[idx1] = nums[idx2]
            nums[idx2] = temp

        swap(i, leftDex)

        # after replacement, the right half is still in reversed sorted order, so reverse
        # to get the actual sorted order
        nums[leftDex + 1:] = nums[leftDex + 1 :][::-1]
        
    
        
        





            






        
# @lc code=end

