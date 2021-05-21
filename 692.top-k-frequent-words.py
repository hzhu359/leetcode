#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res = []
        heap = []

        # frequencies
        ddict = defaultdict(int)
        for word in words:
            ddict[word] += 1

        for key, value in ddict.items():
            heap.append( (-1 * value, key) )

        heapq.heapify(heap)

        while k > 0:
            currFreq = heap[0][0]
            sameFreqWords = []
            while heap and heap[0][0] == currFreq:
                sameFreqWords.append(heapq.heappop(heap))
            sameFreqWords.sort(reverse = True)
            while k > 0 and sameFreqWords:
                res.append(sameFreqWords.pop()[1])
                k -= 1
            sameFreqWords.clear()
        
        return res





# @lc code=end

