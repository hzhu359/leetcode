#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        # abcadjtn
        ret = 0
        charSet = set()
        i = 0
        j = 1
        curr = s[i:j] 

        while j <= len(s):
            if curr[len(curr) - 1] in charSet:
                charSet.remove(curr[0])
                i += 1
            else:
                ret = max(ret, len(curr))
                charSet.add(curr[len(curr) - 1])
                j += 1
            curr = s[i:j]
        return ret



# @lc code=end

