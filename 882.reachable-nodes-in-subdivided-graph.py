#
# @lc app=leetcode id=882 lang=python3
#
# [882] Reachable Nodes In Subdivided Graph
#

# @lc code=start
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        import heapq
        from collections import deque
        # edge represented as u, v, cnt

        # simply a set of u, v, cnt (we can use later after dijkstra)
        edgeSet = set()
        
        # map of nodes: map of neighbors to weight 
        adjList = dict()

        for edge in edges:
            u, v, cnt = edge
            adjList.setdefault(u, dict())[v] = cnt + 1
            adjList.setdefault(v, dict())[u] = cnt + 1

            edgeSet.add((min(u, v), max(u, v), cnt + 1))


        dist = [float('inf') for _ in range(n)]
        dist[0] = 0

        prev = [None for _ in range(n)]

        heapDex = 0
        heap = []
        heapq.heappush(heap, (0, heapDex, 0))
        heapDex += 1

        visited = set()

        while heap:
            curr = heapq.heappop(heap)[2]

            if curr in visited:
                continue

            visited.add(curr)

            for nei, weight in adjList.get(curr, dict()).items():
                # relax
                if dist[curr] + weight < dist[nei]:
                    dist[nei] = dist[curr] + weight
                    prev[nei] = curr

                    heapq.heappush(heap, (dist[nei], heapDex, nei))
                    heapDex += 1
        
        print(f'dist {dist}')
        print(f'prev {prev}')

        def getPath(index, path):
            if index is None:
                return path
            path.appendleft(index)
            return getPath(prev[index], path)
        
        ret = 1

        minPathTreeEdgeSet = set()

        for idx in range(n):
            if idx == 0 or dist[idx] > maxMoves:
                continue

            
            path = getPath(idx, deque())
            print(path)
            k = len(path)
            for jdx in range(k):
                if jdx == k - 1:
                    break
                # get edge and weights
                u = path[jdx]
                v = path[jdx + 1]
                weight = adjList[u][v]
                edge = (min(u, v), max(u, v), weight)
                minPathTreeEdgeSet.add(edge)
        
        for edge in minPathTreeEdgeSet:
            ret += edge[2]
        
        remainingEdges = edgeSet.difference(minPathTreeEdgeSet)
        print(remainingEdges)
        print(minPathTreeEdgeSet)
        
        print(f'before rest: {ret}')

        for edge in remainingEdges:
            u, v, weight = edge

            weight -= 1

            ucap = max(0, maxMoves - dist[u])
            vcap = max(0, maxMoves - dist[v])

            ret += min(ucap + vcap, weight)

        return ret

        










        



# @lc code=end

