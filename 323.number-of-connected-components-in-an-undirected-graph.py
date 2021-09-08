#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#

# @lc code=start
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # construct graph
        from collections import defaultdict

        G = defaultdict(set)
        for a, b in edges:
            G[a].add(b)
            G[b].add(a)

        # dfs
        ret = 0
        visited = set()

        def dfs(curr):
            if curr in visited:
                return
            visited.add(curr)

            for neighbor in G[curr]:
                dfs(neighbor)

        for node in range(n):
            if node in visited:
                continue

            ret += 1
            dfs(node)

        return ret


# @lc code=end
