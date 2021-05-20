#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def normalPalindrome(s):
            n = len(s)
            for i in range(n // 2):
                if not s[i] == s[n - 1 - i]:
                    return False
            return True

        '''
        intuition: we have two strings to check:
        1. everything outside of the char to delete
        2. everything inside (after) the char to delete
        so for something like 'abcbza',
        the outside would be 'a...a'
        and the inside would be 'bcb' (after deleting z)
        '''
        n = len(s)
        i = 0

        # advance pointer until we have a mismatch:
        while i < (n // 2) and s[i] == s[n - 1 - i]:
            i += 1
        
        # check if it's a completely valid palindrome:
        if i >= (n // 2):
            return True

        # check the possibility of removing stuff
        j = n - 1 - i

        if s[i] == s[j - 1]:
            if normalPalindrome(s[i:j]):
                return True
        if s[j] == s[i + 1]:
            if normalPalindrome(s[i + 1: j + 1]):
                return True
        return False





# @lc code=end

