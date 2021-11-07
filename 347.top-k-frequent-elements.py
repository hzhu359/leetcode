#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        from collections import Counter
        import heapq

        ret = []

        counts = Counter(nums)

        heap = []
        idx = 0
        for key, val in counts.items():
            heapq.heappush(heap, (-val, key, idx))
            idx += 1
        
        for _ in range(k):
            if heap:
                ret.append(heapq.heappop(heap)[1])
        
        return ret









































        """
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
        """

# @lc code=end

