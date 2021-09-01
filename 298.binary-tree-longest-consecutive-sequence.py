#
# @lc app=leetcode id=298 lang=python3
#
# [298] Binary Tree Longest Consecutive Sequence
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:

        ret = 0

        def dfs(curr):
            nonlocal ret
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right) 
            themax = 0

            # take the max of correct children
            if not curr.left is None and curr.left.val == curr.val + 1:
                themax = max(themax, left)
            if not curr.right is None and curr.right.val == curr.val + 1:
                themax = max(themax, right)

            themax += 1
            ret = max(ret, themax)
            return themax

        dfs(root)
        return ret






# @lc code=end

