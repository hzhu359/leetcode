#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dd = defaultdict(int)
        for num in nums:
            dd[num] += 1
        
        heap = []
        for key, v in dd.items():
            heapq.heappush(heap, (v, key))

            if len(heap) > k:
                heapq.heappop(heap)
            

        ret = []

        while heap:
            ret.append(heapq.heappop(heap)[1])
        
        return ret[::-1]

# @lc code=end

