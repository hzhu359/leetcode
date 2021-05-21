#
# @lc app=leetcode id=1662 lang=python3
#
# [1662] Check If Two String Arrays are Equivalent
#

# @lc code=start
from functools import reduce
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        '''
        using reduce
        '''
        # return reduce(lambda x,y: x + y, word1, "") == reduce(lambda x,y: x + y, word2, "")

        '''
        using join?
        '''
        return ''.join(word1) == ''.join(word2)

        '''
        constructing/deconstructing
        '''
        # word = ""
        # for chunk in word1:
        #     word += chunk

        # for idx in range(len(word2) - 1, 0 - 1, -1):
        #     if word.endswith(word2[idx]):
        #         word = word[:len(word) - len(word2[idx])]
        #     else:
        #         return False
        # return True






# @lc code=end

