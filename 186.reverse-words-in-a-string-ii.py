#
# @lc app=leetcode id=186 lang=python3
#
# [186] Reverse Words in a String II
#

# @lc code=start
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # num of chars in s
        numChars = len(s)

        # num of words in s
        numWords = s.count(" ") + 1

        if numWords == 1:
            return

        # def dfs(i, j, n):
        #     print(i, j, n)
        #     if n == 0 or n == 1:
        #         print("".join(s[i:j]))
        #         return "".join(s[i:j])
            
        #     spacesEncountered = 0
        #     k = i

        #     # odd words, extra on right

        #     while k < j and spacesEncountered < n // 2:
        #         if s[k] == " ":
        #             spacesEncountered += 1
        #         k += 1
        #     k -= 1
            
        #     leftret = dfs(i, k, n // 2)
        #     rightret = dfs(k + 1, j, n // 2 + n % 2)

        #     replace = rightret + " " + leftret

        #     s[i:j] = list(replace)

        #     return replace
        
        # dfs(0, numChars, numWords)

        def recurse(s1, s2):
            if s1 < 0 or s2 >= numChars:
                return

            i = s1 - 1
            j = s2 + 1

            while i >= 0 and s[i] != " ":
                i -= 1
            
            while j < numChars and s[j] != " ":
                j += 1
            
            s[i + 1: j] = s[s2 + 1: j] + s[s1:s2 + 1] + s[i + 1: s1]

            recurse(i, j)

        spEnc = 0
        k = 0

        while k < numChars and spEnc < numWords // 2:
            if s[k] == " ":
                spEnc += 1
            k += 1
        k -= 1

        # k is at the middle space
        # if odd, k is at the left middle space
        
        if not numWords % 2:
            # even case, find middle space
            recurse(k, k)
        else:
            # odd case, find middle word w/ spaces on edges
            l = k + 1
            while l < numChars and s[l] != " ":
                l += 1
            recurse(k, l)






            

        
        
        
# @lc code=end

