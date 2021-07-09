#
# @lc app=leetcode id=1059 lang=python3
#
# [1059] All Paths from Source Lead to Destination
#

# @lc code=start
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        from collections import defaultdict
        # ANY cycle = false
        # dfs should return if a branch ends up always at dest.
        #   if at any point the termini are not dest, return False
        # destination must be connected to source somehow
        # dfs bih

        visited = [False for _ in range(n)]
        adjList = defaultdict(list)

        for edge in edges:
            adjList[edge[0]] = edge[1]

        if adjList[destination]:
            return False
        
        # finding cycles for directed graphs????
        

        
        

            


            


                
        




# @lc code=end

