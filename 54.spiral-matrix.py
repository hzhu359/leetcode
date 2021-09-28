#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # dfs and track visited by setting to None

        dirs = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
        m, n = len(matrix), len(matrix[0])
        ret = []

        def dfs(curr, dir):
            y, x = curr
            # check invalid
            if y < 0 or y >= m or x < 0 or x >= n or matrix[y][x] is None:
                return False

            # mark visited
            ret.append(matrix[y][x])
            matrix[y][x] = None

            # move in direction
            dy, dx = dirs[dir]
            nextcurr = [y + dy, x + dx]
            result = dfs(nextcurr, dir)

            # if invalid turn and move there
            if not result:
                dir = (dir + 1) % 4
                dy, dx = dirs[dir]
                nextcurr = [y + dy, x + dx]
                result = dfs(nextcurr, dir)

            # else
            return True
        
        dfs((0,0), 0)
        return ret


# @lc code=end

