#
# @lc app=leetcode id=1168 lang=python3
#
# [1168] Optimize Water Distribution in a Village
#

# @lc code=start
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        from collections import defaultdict
        import heapq

        # union-find
        parent = [-1 for _ in range(n + 1)]
        # union find has two things
        # find parent
        def find(x):
            if parent[x] == -1:
                return x
            return find(parent[x])
        
        # union into group
        def union(x, y):
            parent[find(x)] = find(y)
        
        def unionFind(x, y):
            if find(x) == find(y):
                return False
            union(x, y)
            return True


        pipes += [[idx + 1, 0, wells[idx]] for idx in range(n)]
        h = []
        qindex = 0
        for pipe in pipes:
            heapq.heappush(h, (pipe[2], qindex, pipe))
            qindex += 1
        
        # trees have n nodes and n - 1 edges
        ret = 0
        edgeNum = 0
        while h and edgeNum < (n + 1) - 1:
            curr = heapq.heappop(h)
            currPipe = curr[-1]
            print(curr)
            cond = unionFind(currPipe[0], currPipe[1])
            print(cond)

            if cond:
                edgeNum += 1
                ret += currPipe[-1]
            
        print(parent)
        return ret



# @lc code=end

