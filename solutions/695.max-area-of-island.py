#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ret = 0

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != 1:
                return 0
            
            grid[i][j] = 0

            ret = 1
            ret += dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i, j - 1)


            return ret

        for i in range(n):
            for j in range(m):
                curr = grid[i][j]
                if curr == 1:
                    ret = max(ret, dfs(i, j))
        
        return ret



            


        
# @lc code=end

