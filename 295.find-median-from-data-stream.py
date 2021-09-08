#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
from heapq import heappop, heappush, heappushpop


class MedianFinder:
    import heapq

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxOfMinHalf = []
        self.minOfMaxHalf = []

    def addNum(self, num: int) -> None:
        top = heappushpop(self.maxOfMinHalf, -1 * num)
        heappush(self.minOfMaxHalf, -1 * top)

        if len(self.maxOfMinHalf) < len(self.minOfMaxHalf):
            heappush(self.maxOfMinHalf, -1 * heappop(self.minOfMaxHalf))

        # print(self.maxOfMinHalf, self.minOfMaxHalf)

    def findMedian(self) -> float:
        # print(self.maxOfMinHalf, self.minOfMaxHalf)
        if len(self.maxOfMinHalf) > len(self.minOfMaxHalf):
            return -1 * self.maxOfMinHalf[0]
        else:
            return (-1 * self.maxOfMinHalf[0] + self.minOfMaxHalf[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
