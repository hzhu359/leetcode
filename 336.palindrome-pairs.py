#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#

# @lc code=start


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        from collections import defaultdict
        from itertools import product

        def isPalindrome(word):
            for i in range(len(word) // 2):
                if not word[i] == word[len(word) - 1 - i]:
                    return False
            return True

        def palindromeSides(word, idx, leftmap, rightmap):
            """
            our goal here is to find palindromes within the string
            s.t. we're able to append some string to the left/right hand side of the string
            to make that extended string also a palindrome

            i.e. for the string 'llghg'

            we have an inner palindrome 'l',
            so we can prepend the rest of the string reversed in order to continue a palindrome
            rev('lghg') + 'llghg' = 'ghgl' + 'llghg' = 'ghglllghg

            we also have 'll' -> rev('ghg') + 'llghg' = 'ghgllghg'

            we have no more palindromes starting at index 0, so look to the right

            we have 'g' and 'ghg', so append the reverses on the right side
            'g' -> 'llghghgll', 'ghg' -> 'llghgll'
            """
            n = len(word)

            # dromes starting at 0, add reversed rest of word to lefts
            for i in range(n + 1):
                curr = word[:i]
                if isPalindrome(curr):
                    leftmap[word[i::][::-1]].add(idx)

            for i in range(n, 0 - 1, -1):
                curr = word[i:]
                if isPalindrome(curr):
                    rightmap[word[:i:][::-1]].add(idx)

        # words.sort(key=lambda x: len(x))

        # maps k, v s.t. k + words[v] = palindrome
        leftmap = defaultdict(set) 
        # maps k, v s.t. words[v] + k = palindrome
        rightmap = defaultdict(set) 

        for idx, word in enumerate(words):
            palindromeSides(word, idx, leftmap, rightmap)
        
        # print(words)
        # print(leftmap)
        # print(rightmap)

        ret = set()

        for idx, word in enumerate(words):
            # make sure we're not doing (1,1)

            # left
            if word in leftmap:
                ret.update([x for x in product([idx], leftmap[word]) if x[0] != x[1]])

                # if word == "":
                #     print(idx)
                #     print(leftmap[word])
                #     print([x for x in product([idx], leftmap[word])])
            # right
            if word in rightmap:
                ret.update([x for x in product(rightmap[word], [idx]) if x[0] != x[1]])
        
        return ret
    



# @lc code=end
