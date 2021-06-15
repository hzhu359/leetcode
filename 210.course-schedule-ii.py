#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        we know that topological sort gives us some ordering of nodes such that each edge
        is a lower to higher index
        in dags, each edge is from a higher to lower post number, so a topological sort would be the reverse postorder

        now we have to figure out
        1. how to root our tree
            if we find some node with 0 prereqs
        2. how to do dfs on our tree
            create an adjacency list upon which we can recurse

        the return will be formed by appending to the front of a deque each time a node gets closed
        (i.e. each time a node returns from recursion and gets a postnumber)

        it will be impossible to finish if our deque's length is less than numCourses
        or if our tree is not a dag (i.e. there are cycles of prerequisites)

        maintain an adjacency list, a visited set, and a return deque
        '''

        '''
        toposort method
        '''

        '''
        from collections import deque, defaultdict

        # adjacency list will be map: node -> outneighbors (so we can recurse on them)
        adjList = defaultdict(set)
        visited = [False for _ in range(numCourses)]
        ret = deque()
        retList = [False for _ in range(numCourses)]
        intros = set([i for i in range(numCourses)])

        # populate a graph
        for course, prereq in prerequisites:
            intros.difference_update({course})
            adjList[prereq].add(course)
        
        def dfs(v):
            if visited[v]:
                return
            visited[v] = True
            for neighbor in adjList[v]:
                dfs(neighbor)
                if not retList[neighbor]:
                    return []
            ret.appendleft(v)
            retList[v] = True
        
        for v in intros:
            dfs(v)

        if len(ret) == numCourses:
            return list(ret)
        else:
            return []
        '''

        '''
        toposort 2 method (build by indegrees)
        '''
        from collections import defaultdict

        indegrees = [0 for _ in range(numCourses)]
        adjList = defaultdict(set)
        ret = []
        q = []

        for course, prereq in prerequisites:
            adjList[prereq].add(course)
            indegrees[course] += 1
        
        for course, indeg in enumerate(indegrees):
            if indeg == 0:
                q.append(course)
        
        while q:
            curr = q.pop()
            ret.append(curr)

            for neighbor in adjList[curr]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)
            
            # for neighbor in adjList[curr]:
            #     q.append(neighbor)
        
        return ret if len(ret) == numCourses else []


        


# @lc code=end

