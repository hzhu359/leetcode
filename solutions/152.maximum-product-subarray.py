#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
from functools import reduce
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        '''
        ok so your intuition in v1 was kind of ok
        for all of these you'll be continuously multiplying along to maintain contiguity
        for 0s: if you're moving along and encounter a zero, your chain of multiplication
            is reset to zero and you must start over again
        for negatives: if you encounter one, it flips your result negative,
            but if you encounter another, your result flips back positive
            for this reason, we have to keep track of a min value (
                the minimum contiguously-accessible subarray product
                up to that point
            )
            the min value will allow us to multiply an encountered negative
                to flip positive again
        
        subproblem: maximize some choices (these choices always involve current
            such that contiguity is conserved).
            also a "global" max will be taken after each maximization of these choices

            1. stay with current (nums[i])
            2. multiply by maximum accessible array (in the positive case)
            3. multiply by minimum accessible array (in the negative case)
        '''
        # stores maximum/minimum accessible contiguous arrays that we'll multiply by
        if not nums:
            return 0

        max_cont = nums[0] 
        min_cont = nums[0] 

        # our "global" max that we'll return
        ret = nums[0]

        # setting up dp array
        n = len(nums)

        for idx in range(1, n):
            max_cont, min_cont = \
                max(nums[idx], nums[idx] * max_cont, nums[idx] * min_cont),\
                min(nums[idx], nums[idx] * max_cont, nums[idx] * min_cont)
            ret = max(ret, max_cont)
        
        return ret


    # def maxProduct(self, nums: list[int]) -> int:
    #     '''
    #     before this, split all arrays by 0!
    #     this allows us to not have to consider 0 (because we wouldn't want to anyways)

    #     cases:
    #     1. even number of negatives
    #         use regular ol' kadane's to solve this
    #         (note we can't just return the complete product due to zeroes)
    #         so just track the maximal subarray products with negatives inverted to positive
    #     2. odd number of negatives
    #         we can cut off ONE negative (on either end) to determine maximal product
    #         so if we have [pos, pos, neg, neg, pos, neg, pos, pos],
    #         we have 3 negatives and (bookend) negatives at indices 2 and 5
    #         so we run kidanes such that all negatives (except for each ending)
    #             are inverted to positive
        
    #     naively running kidane's here will pretty much separate the array into
    #     different subarrays without the negatives considered
        
    #     thus for evens, we flip negatives because we want a naive kidane's on

    #     NOTE! THIS IS THE WORST IMPLEMENTATION ! DON'T DO THIS!
    #     '''

    #     if len(nums) == 0:
    #         return 0
    #     if len(nums) == 1:
    #         return nums[0]

    #     zeroSplit = []
    #     startSplit = 0
        
    #     for idx, num in enumerate(nums):
    #         if num == 0:
    #             arr = nums[startSplit : idx]
    #             if arr:
    #                 zeroSplit.append(arr)
    #             startSplit = idx + 1

    #     if startSplit != 0:
    #         zeroSplit.append([0])

    #     if nums[startSplit:]:
    #         zeroSplit.append(nums[startSplit:])


        
    #     print(zeroSplit)

    #     ret = float('-inf')
    #     for split in zeroSplit:
    #         negIdx = self.countNegs(split)
    #         if len(split) == 1:
    #             # one length case
    #             ret = max(ret, split[0])
    #         elif len(negIdx) % 2 == 0:
    #             # even case
    #             ret = max(ret, reduce(lambda x, y: x * y, split, 1))
    #         else:
    #             # odd case
    #             firstNegIdx = negIdx[0]
    #             lastNegIdx = negIdx[len(negIdx) - 1]
    #             ret = max(ret, reduce(lambda x, y: x * y, split[0:firstNegIdx], 1))
    #             ret = max(ret, reduce(lambda x, y: x * y, split[firstNegIdx + 1:], 1))
    #             ret = max(ret, reduce(lambda x, y: x * y, split[0:lastNegIdx], 1))
    #             ret = max(ret, reduce(lambda x, y: x * y, split[lastNegIdx + 1:], 1))

    #     return int(ret)

    def countNegs(self, nums):
        ret = []
        for idx, num in enumerate(nums):
            if num < 0:
                ret.append(idx)
        return tuple(ret)


# @lc code=end

