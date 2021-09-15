#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#

# @lc code=start
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # trees are acyclic, connected
        from collections import defaultdict

        g = defaultdict(set)

        for u, v in edges:
            g[u].add(v)
            g[v].add(u)

        visited = set()

        def dfs(curr, parent):
            if curr is None:
                return True

            if curr in visited:
                return False
            
            visited.add(curr)
            
            for nei in g[curr].difference({parent}):
                if not dfs(nei, curr):
                    return False
            
            return True

        if dfs(0, -1):
            return len(visited) == n
        
        return False





# @lc code=end

