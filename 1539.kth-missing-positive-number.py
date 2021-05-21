#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        present = set(arr)
        # maxElem = max(arr)
        idx = 1
        count = 1

        while True:
            # if idx > maxElem:
            #     break
            if not idx in present:
                if count == k:
                    return idx
                count += 1
            idx += 1

        # return maxElem + k - (count - 1)


# @lc code=end

