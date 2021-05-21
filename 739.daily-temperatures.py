#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        res = [0 for _ in range(n)]

        for i in range(n - 2, 0 - 1, -1):
            j = i + 1
            while (j < n):
                if T[i] < T[j]:
                    res[i] = j - i
                    break
                elif res[j] == 0:
                    res[i] = 0
                    break
                else:
                    j += res[j]
        
        return res





# @lc code=end

