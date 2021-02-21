#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        ret = 0

        while i <= j:
            weight = people[i] + people[j]

            if weight > limit:
                j -= 1
            else:
                i += 1
                j -= 1

            ret += 1
        
        return ret

# @lc code=end

