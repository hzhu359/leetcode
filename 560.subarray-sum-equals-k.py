#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        naive sum array
        '''
        # ret = 0
        # for idx in range(len(nums)):
        #     tot = 0
        #     for jdx in range(idx, len(nums)):
        #         tot += nums[jdx]
        #         ret += 1 if tot == k else 0

        # return ret

        '''
        hashmap thing
        '''
        # our return result (accumulator)
        ret = 0

        # the dict that maps the number of current running sums
        #   to the number of occurrences
        sumDict = defaultdict(int)

        # our running sum
        runSum = 0

        # initiating 0 in our running sum
        sumDict[runSum] += 1


        # loop through our array
        for num in nums:
            # update runSum
            runSum += num
            # initiate a "target"
            #   pretty much denotes what we're looking for in the sumDict
            #   if the current sum of [0...i] minus the k we're looking for,
            #   then that means some sum [0...j] has existed such that
            #   sum[0...i](runsum) - sum[0...j](target) == k
            #   so
            #   sum[j...i] == k
            target = runSum - k

            # iterate our accumulator by the number of times that our target has been hit b4
            ret += sumDict[target]

            # iterate our sumDict
            sumDict[runSum] += 1
        return ret

# @lc code=end

