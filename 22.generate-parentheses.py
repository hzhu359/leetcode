#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        the key here is to note that you only have two options:
        1. add a open paren
        2. add a close paren

        then you know the constraints of what you can and can not do
        '''

        def dfs(parens, opeen, close, n, ret):
            if close == n:
                ret.append(parens)
                return
            
            if opeen < n:
                dfs(parens + '(', opeen + 1, close, n, ret)
            if close < n and opeen > close:
                dfs(parens + ')', opeen, close + 1, n, ret)


        ret = []
        dfs('', 0, 0, n, ret)
        return ret


        
# @lc code=end

