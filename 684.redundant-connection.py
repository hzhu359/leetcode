#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict

        visited = [False for i in range(len(edges) + 1)]

        adjList = defaultdict(list)
        for e in edges:
            adjList[e[0]].append(e[1])
            adjList[e[1]].append(e[0])
        
        # cyclist = []
        retset = set()

        start = None

        def dfs(curr, par):
            nonlocal start
            if visited[curr]:
                start = curr
                retset.add((curr, par))
                retset.add((par, curr))
                return True

            visited[curr] = True

            # recurse on non-parents
            for v in filter(lambda x: x != par, adjList[curr]):
                ret = dfs(v, curr)
                if ret:
                    if curr != start:
                        retset.add((curr, par))
                        retset.add((par, curr))
                        return ret
                    else:
                        return False
            
            return False
        
        dfs(1, None)


        # for i in range(len(cyclist) - 1):
        #     retset.add((cyclist[i], cyclist[i + 1]))
        #     retset.add((cyclist[i + 1], cyclist[i]))
        
        for e in reversed(edges):
            if tuple(e) in retset:
                return e

        return None





# @lc code=end

