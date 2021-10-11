#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # EVERY path must be evaluated at some highest point
        # at this highest point
        #   (and only one highest point exists since paths in trees
        #   cannot go up to the same level since no cycles)
        # you can either use
        # this point and its left,
        # this points and its right,
        # this point and go left and right
        # or stop just at this point

        ret = float("-inf")

        def dfs(curr):
            nonlocal ret
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            localRet = curr.val + max(left, right, 0)
            ret = max(ret, localRet, curr.val + left + right)
            return localRet

        dfs(root)

        return ret


# @lc code=end
