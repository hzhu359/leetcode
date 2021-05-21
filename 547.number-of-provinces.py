#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#
# @lc code=start
from collections import deque
class Solution:
    """
    hehe
    """
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        # returns ~an~ element of a set
        def sampleSet(mySet):
            for x in mySet:
                return x

        n = len(isConnected)
        unvisited = set(range(n))

        # use popleft and append
        q = deque([])

        ret = 0

        while unvisited:
            q.append(sampleSet(unvisited))
            while q:
                curr = q.popleft()
                unvisited.discard(curr)

                for idx, x in enumerate(isConnected[curr]):
                    if x == 1 and idx in unvisited:
                        deque.append(idx)
            ret += 1
        return ret



        


# @lc code=end