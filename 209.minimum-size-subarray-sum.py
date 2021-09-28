#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 9/27 sol
        # keep a sliding window and extend right if you must
            # in that case, just add on the right addition
        # contract from left if we satisfy
            # in that case, just subtract the leftmost

        i = 0
        j = 0

        n = len(nums)
        ret = n + 1

        curr = 0

        while j < n and i < n:
            # edge case where i == j?

            if curr < target:
                # expand
                curr += nums[j]
                j += 1

            else: # if curr >= target
                # mark down and contract
                ret = min(ret, j - i)
                curr -= nums[i]
                i += 1

        while i < n and curr >= target:
            ret = min(ret, j - i)
            curr -= nums[i]
            i += 1
        
        return 0 if ret == n + 1 else ret


        # import itertools
        # import bisect

        '''
        naive
        run through subarrays of size 1 thru n
        n = len(nums)
        maxEntry = nums[0]
        for entry in nums:
            maxEntry = max(maxEntry, entry)
        '''

        # for k in range( math.ceil(target / maxEntry), n + 1):
        #     # init
        #     windowSum = sum(nums[0:k])
        #     if windowSum >= target:
        #         return k

        #     for i in range(k, n):
        #         windowSum -= nums[i - k]
        #         windowSum += nums[i]
        #         if windowSum >= target:
        #             return k
        
        # return 0

        '''
        smarter
        use [0...i] sums to find subarray sums
        start from each index and find the minimum subarray sum
        that sums to the target
        target <= sum[i...j] = sum[0...j] - sum[0...i - 1]
        target <= sum = b - a
        b >= a + target
        so for each [0...i] sum `a` find some `b` (search for it) geq a + target
        '''

        # subsum = list(itertools.accumulate(nums))
        # n = len(subsum)
        # res = n
        # print(subsum)

        # if subsum[res - 1] < target:
        #     return 0
        

        # b = target
        # matchDex = bisect.bisect_left(subsum, b)
        # if matchDex != n:
        #     res = min(res, matchDex + 1)

        # for idx, entry in enumerate(subsum):
        #     b = entry + target
        #     matchDex = bisect.bisect_left(subsum, b)
        #     if matchDex == n:
        #         continue
        #     res = min(res, matchDex - idx)
        
        # return res

        '''
        even smarter?
        in any given sliding window, we're guaranteed that the sum will
            - increase if we extend its tail to the right
            - decrease if we contract its head to the right

        then for a sliding window nums[i...j + 1] (exclusive),
        we know that the minimum target-sum subarray ending at j can be
        sussyed out by just moving i (decreasing)
        until it no longer hits that target-sum

        then when we no longer hit the target-sum,
        move j right until we do (increase)
        '''

        # i = 0
        # j = 1
        # runSum = nums[0]
        # n = len(nums)
        # res = n

        # endRunSum = runSum

        # while j < n:
        #     # check valid
        #     if runSum >= target: # try decreasing
        #         endRunSum = runSum
        #         res = min(res, j - i)
        #         runSum -= nums[i]
        #         i += 1
        #     else: # if runSum < target, try increasing
        #         runSum += nums[j]
        #         j += 1
        
        # # must handle j == n (subarray of [i...n])

        # while runSum >= target:
        #     endRunSum = runSum
        #     res = min(res, j - i)
        #     endRunSum = runSum
        #     runSum -= nums[i]
        #     i += 1

        
        # return res if endRunSum >= target else 0
        













# @lc code=end

