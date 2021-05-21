#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        last = None
        ret = 0
        combo = 0
        idx = 0

        for c in (chars + [0]):
            if c == last:
                combo += 1
            else:
                if combo == 0:
                    pass 
                elif combo == 1:
                    ret += 1
                    chars[idx] = last 
                    idx += 1
                else:
                    ret += (1 + len(str(combo)))
                    chars[idx] = last 
                    idx += 1

                    for num in str(combo):
                        chars[idx] = num
                        idx += 1
                last = c
                combo = 1
        
        return ret




        
# @lc code=end

