#
# @lc app=leetcode id=413 lang=python3
#
# [413] Arithmetic Slices
#

# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        def getThreeSubs():
            ret = set()
            curr = 2 

            while curr < n:
                rdiff = nums[curr] - nums[curr - 1]
                ldiff = nums[curr - 1] - nums[curr - 2]

                if rdiff == ldiff:
                    ret.add((curr - 2, curr, rdiff))
                curr += 1
            
            return ret

        
        visited = set()

        def dfs(curr):
            if curr in visited:
                return
            
            visited.add(curr)

            i, j, diff = curr

            # left extend
            if i - 1 >= 0 and diff == nums[i] - nums[i - 1]:
                dfs((i - 1, j, diff))

            # right extend
            if j + 1 < n and diff == nums[j + 1] - nums[j]:
                dfs((i, j + 1, diff))


        for threeSub in getThreeSubs():
            dfs(threeSub)
        
        return len(visited)

 





# @lc code=end

