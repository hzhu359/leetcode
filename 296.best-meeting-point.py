#
# @lc app=leetcode id=296 lang=python3
#
# [296] Best Meeting Point
#

# @lc code=start


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # naive: save a set of house coords
        # for each 0 in the matrix, calculate sum of manhattans
        # save minimum
        
        m = len(grid)
        n = len(grid[0])

        mlist = []

        for i in range(m):
            for j in range(n):
                # sorts by i, gets sorted vertical vals
                if grid[i][j] == 1:
                    mlist.append(i)
        
        nlist = []

        for j in range(n):
            for i in range(m):
                # sorts by j, gets sorted horiz vals
                if grid[i][j] == 1:
                    nlist.append(j)
        
        mlen = len(mlist)
        mmed = mlist[mlen // 2] if mlen % 2 else (mlist[mlen // 2] + mlist[mlen // 2 - 1]) // 2
        nlen = len(nlist)
        nmed = nlist[nlen // 2] if nlen % 2 else (nlist[nlen // 2] + nlist[nlen // 2 - 1]) // 2

        print(mlist)
        print(nlist)
        print(mmed, nmed)
    
        ret = 0
        for m in mlist:
            ret += abs(m - mmed)
        for n in nlist:
            ret += abs(n - nmed)
        
        return ret

# @lc code=end

