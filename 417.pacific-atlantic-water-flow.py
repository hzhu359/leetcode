#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # naively
        # bfs on every node and see if it can get to the ocean
        # if we bfs to a node that is already proven, return true early

        m = len(heights)
        n = len(heights[0])

        memoSet = set()

        def dfs(curr, pacific, atlantic, visited):
            if curr in visited:
                return -1

            if curr in memoSet:
                return 2

            # 0 - touched pacific, 1 - touched atlantic, 2 - touched both
            # dfs in all directions and see what it touches
            visited.add(curr)
            i, j = curr[0], curr[1]

            if i == 0 or j == 0:
                pacific = True

            if i == m - 1 or j == n - 1:
                atlantic = True

            if atlantic and pacific:
                return 2

            for coord in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if coord[0] < 0 or coord[1] < 0 or coord[0] >= m or coord[1] >= n:
                    continue
                if heights[coord[0]][coord[1]] <= heights[curr[0]][curr[1]]:
                    res = dfs(coord, pacific, atlantic, visited)
                    if res == 0:
                        pacific = True
                    if res == 1:
                        atlantic = True
                    if res == 2:
                        pacific = atlantic = True

            if pacific and not atlantic:
                return 0
            if atlantic and not pacific:
                return 1
            if atlantic and pacific:
                return 2
            return -1

        ret = set()

        for i in range(m):
            for j in range(n):
                if dfs((i, j), False, False, set()) == 2:
                    ret.add((i, j))
                    memoSet.add((i, j))

        return ret


# @lc code=end
