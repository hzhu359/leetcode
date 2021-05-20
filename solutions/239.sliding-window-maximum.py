#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # keep a monotonically decreasing deque
        deq = deque()

        def reset(i):
            if len(deq) == 0:
                return
            # pop off left index
            if deq[0] <= i - k:
                deq.popleft()
            # pop off smaller indices from tail
            while len(deq) != 0 and not (nums[deq[-1]] > nums[i]):
                deq.pop()
        
        output = []
        maxIndex = 0

        for i in range(k):
            reset(i)
            deq.append(i)
            if nums[deq[0]] > nums[maxIndex]:
                maxIndex = deq[0]
            
        output.append(nums[maxIndex])

        for i in range(k, len(nums)):
            reset(i)
            deq.append(i)
            output.append(nums[deq[0]])
        
        return output

# @lc code=end

