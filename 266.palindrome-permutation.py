#
# @lc app=leetcode id=266 lang=python3
#
# [266] Palindrome Permutation
#

# @lc code=start
from collections import defaultdict
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = defaultdict(int)
        for char in s: 
            counts[char] += 1
        
        oddCount = 0
        for char, count in counts.items():
            if count % 2 != 0:
                oddCount += 1
                if oddCount > 1:
                    return False
        return True

# @lc code=end

