#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        maintain a stack of open parentheses '(' locations
        if ever we encounter a close parentheses ')' without something on the stack,
            remove that close parentheses
        if at the end of the iteration we hvae open parentheses,
            remove those indices from the string
        '''
        arr = list(s)
        stack = []

        for idx, c in enumerate(arr):
            if c == '(':
                stack.append(idx)
            elif c == ')':
                if not stack:
                    arr[idx] = ''
                else:
                    stack.pop()
        
        for idx in stack:
            arr[idx] = ''
        
        return ''.join(arr)
# @lc code=end

