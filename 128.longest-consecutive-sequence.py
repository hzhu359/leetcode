#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seen = set()
        for num in nums:
            seen.add(num)

        ret = 0
        for num in nums:
            if num - 1 in seen:
                # start at minimum of streak!
                continue

            curr = 1
            currNum = num

            while currNum + 1 in seen:
                curr += 1
                currNum += 1
            
            ret = max(ret, curr)
        
        return ret


        
# @lc code=end

