#
# @lc app=leetcode id=1855 lang=python3
#
# [1855] Maximum Distance Between a Pair of Values
#

# @lc code=start
class Solution:
    import bisect
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        ret = 0
        while i < len(nums1) and j < len(nums2):
            if i <= j:
                if nums1[i] <= nums2[j]:
                    ret = max(ret, j - i)
                    j += 1
                else:
                    i += 1
            else:
                j = i
        
        return ret


# @lc code=end

