#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        i = 0
        n = len(nums)
        # set a default ret
        ret = nums[0] + nums[1] + nums[2]

        while i < n - 2:
            j = i + 1
            k = n - 1

            while (j < k):
                # update                            
                threeSum = nums[i] + nums[j] + nums[k]
                if abs(target - threeSum) < abs(target - ret):
                    ret = threeSum
                            
                # move
                if target - threeSum == 0:
                    return ret                  
                elif target - threeSum > 0: # must increase ret
                    j += 1
                elif target - threeSum < 0: # must decrease ret
                    k -= 1
            i += 1
        
        return ret

# @lc code=end

