#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(curr):
            if p.val <= curr.val <= q.val:
                return curr
            if curr.val < p.val:
                return dfs(curr.right)
            elif curr.val > q.val:
                return dfs(curr.left)
        if p.val > q.val:
            p, q = q, p
        return dfs(root)








# @lc code=end

