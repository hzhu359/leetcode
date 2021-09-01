#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#

# @lc code=start
class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        
        def canExtend(x, y):
            ret = False

            for i in range(len(y)):
                if x == y[:i] + y[i + 1:]:
                    ret = True
            
            return ret

        n = len(words)
        ret = -1
        words.sort(key=lambda x: len(x))
        lenMap = dict()

        for idx, word in enumerate(words):
            lenMap.setdefault(len(word), idx)
        
        dp = []
        for word in words:
            if len(word) - 1 in lenMap:
                start = lenMap.get(len(word) - 1)

                localmax = 1 
                while start < n and len(words[start]) == len(word) - 1:
                    if canExtend(words[start], word):
                        localmax = max(localmax, dp[start] + 1)
                    start += 1
                
                dp.append(localmax)
                
            else:
                dp.append(1)
            
            ret = max(ret, dp[-1])
        return ret








# @lc code=end

