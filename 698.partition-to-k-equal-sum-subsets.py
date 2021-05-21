#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # nums.sort(reverse = True)
         
        # n = len(nums)
        # numSum = sum(nums)

        # if numSum % k:
        #     return False

        # targetSum = numSum // k

        # visited = [0 for _ in range(n)]

        # def dfs(index, currK, curSum):
        #     if currK == 0:
        #         return True

        #     if curSum == targetSum:
        #         # start over with k - 1 groups
        #         return dfs(0, currK - 1, 0)
            
        #     for i in range(index, n):
        #         if not visited[i] and (nums[i] + curSum <= targetSum):
        #             visited[i] = 1
        #             dfsResult = dfs(i + 1, currK, nums[i] + curSum)
        #             if dfsResult:
        #                 return True
        #             visited[i] = 0

        # return dfs(0, k, 0)
                
        





# @lc code=end

