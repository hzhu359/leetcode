#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 9/27 sol. 

        n = len(s)
        ret = 0
        i, j = 0, 0

        stringset = set()

        while i < n and j < n:
            # expand
            if not s[j] in stringset:
                stringset.add(s[j])
                j += 1
                ret = max(j - i, ret)
            # contract until valid
            else:
                while s[j] in stringset:
                    stringset.remove(s[i])
                    i += 1
        
        return ret
        
        # prev. sol

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

