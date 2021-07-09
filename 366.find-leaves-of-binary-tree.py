#
# @lc app=leetcode id=366 lang=python3
#
# [366] Find Leaves of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        from collections import defaultdict, deque

        ret = defaultdict(list)

        def dfs(curr):
            if not curr:
                return 0

            currLevel = max(dfs(curr.left), dfs(curr.right)) + 1
            ret[currLevel].append(curr.val)
            return currLevel

        dfs(root)

        i = 1
        rett = []

        while(i in set(list(ret))):
            rett.append(ret[i])
            i += 1

        return rett

            



# @lc code=end

