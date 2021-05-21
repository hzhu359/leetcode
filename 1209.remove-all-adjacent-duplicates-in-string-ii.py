#
# @lc app=leetcode id=1209 lang=python3
#
# [1209] Remove All Adjacent Duplicates in String II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        def processString(inStr, idx, k):
            n = len(inStr)
            if idx > n:
                return inStr
            
            lastChar = None
            lastDex = None
            count = None


            while idx < n:
                if not inStr[idx] == lastChar:
                    lastChar = inStr[idx]
                    lastDex = idx
                    count = 1
                else:
                    count += 1
                    if count == k:
                        res = processString(inStr[:lastDex] + inStr[idx + 1:], lastDex, k)
                        return res
                idx += 1
            
            return inStr 
        
        while True:
            res = processString(s, 0, k)
            if res == s:
                return res
            s = res



# @lc code=end

