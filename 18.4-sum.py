#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        from bisect import bisect
        def twoSum(low, hi, twoTarget):
            ret = set()
            while low < hi:
                if nums[low] + nums[hi] == twoTarget:
                    ret.add(tuple([nums[low], nums[hi]]))
                    low += 1
                    hi -= 1
                if nums[low] + nums[hi] < twoTarget:
                    low += 1
                if nums[low] + nums[hi] > twoTarget:
                    hi -= 1
            return ret
        
        def threeSum(low, hi, threeTarget):
            ret = set()
            curr = low
            while low < hi - 1:
                if curr == low or nums[curr - 1] != nums[curr]:
                    for twos in twoSum(low + 1, hi, threeTarget - nums[low]):
                        ret.add(tuple((nums[low],) + twos))
                low += 1
            return ret
        
        nums.sort()
        low = 0
        hi = len(nums) - 1
        ret = set()
        curr = low
        while low < hi - 1:
            if curr == low or nums[curr - 1] != nums[curr]:
                for threes in threeSum(low + 1, hi, target - nums[low]):
                        ret.add(tuple((nums[low],) + threes))
            low += 1
        
        print(ret)
        return ret




# @lc code=end

