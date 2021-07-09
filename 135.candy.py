#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        allocation = [0 for _ in range(n)]

        def greaterThanOrZero(x, y):
            return 0 if ratings[x] >= ratings[y] else allocation[x]

        def maxNeighborVal(idx):
            # edit: throw out any comparisons where ratings[neigh] >= ratings[idx]
            if idx == 0:
                return greaterThanOrZero(1, idx)
            elif idx == n - 1:
                return greaterThanOrZero(n-2, idx)
            
            left = greaterThanOrZero(idx-1,idx)
            right = greaterThanOrZero(idx + 1, idx)
            return max(left, right)

        indexlist = [(idx, entry) for idx, entry in enumerate(ratings)]
        indexlist.sort(key=lambda x: x[1])
        ret = 0

        # indexlist will be sorted based on ~values~, so the indices will be what we're looking at here
        for idx, entry in indexlist:
            val = maxNeighborVal(idx) + 1
            allocation[idx] = val 
            ret += val 
        
        return ret


# @lc code=end

