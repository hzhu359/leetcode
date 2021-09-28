#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from typing import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i, j = 0, 0
        n = len(s)
        ret = []

        stringset = Counter(p) 
        ogset = set(p)

        while i < n and j < n:
            # expand when we knock off a string
            curr = s[j]
            if curr in stringset:
                stringset[curr] -= 1
                if stringset[curr] == 0:
                    stringset.pop(curr)
                j += 1
                if not stringset:
                    ret.append(i)
            # contract when we can't
            else:
                if s[i] in ogset:
                    stringset[s[i]] = stringset.get(s[i], 0) + 1
                i += 1
                j = max(i, j)
        return ret


# @lc code=end
