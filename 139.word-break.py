#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def __init__(self):
        self.cache = {}

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        if not s:
            return True
        if s in wordDict:
            return True
        if s in self.cache:
            return self.cache[s]

        for word in wordDict:
            breakCheckVal = self.breakCheck(s, word)
            if not breakCheckVal:
                continue
            ret = self.wordBreak(s[len(word):], wordDict)
            if ret:
                self.cache[s] = True
                return True
        self.cache[s] = False
        return False


    def breakCheck(self, s: str, pattern: str):
        try:
            ret = s.index(pattern)
            if ret != 0:
                raise Exception()
            return True
        except Exception:
            return False
# @lc code=end

