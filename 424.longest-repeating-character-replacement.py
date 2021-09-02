#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def index(c):
            return ord(c) - ord("A")

        ret = commonChar = nonCommon = window = 0
        occs = [0 for _ in range(26)]

        for idx, c in enumerate(s):
            occs[index(c)] += 1
            commonChar = max(commonChar, occs[index(c)])
            nonCommon = window - commonChar

            if nonCommon >= k:
                # must resize window
                occs[index(s[idx - window])] -= 1
            else:
                window += 1

            ret = max(ret, window)

        return ret


# @lc code=end
