#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    # def canJump(self, nums: List[int]) -> bool:
    def canJump(self, nums):
        n = len(nums)
        reach = nums[0]
        i = 1
        while (i < n - 1) and i <= reach:
            reach = max(reach, i + nums[i])
            i += 1
        return True if reach >= n - 1 else False





# if __name__ == '__main__':
#     sol = Solution()
#     nums = [0,2,3]
#     print(sol.canJump(nums))








# @lc code=end

