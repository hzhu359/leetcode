#
# @lc app=leetcode id=1120 lang=python3
#
# [1120] Maximum Average Subtree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:

        ret = None

        def dfs(curr):
            nonlocal ret
            # must account for both subtree sum and number of nodes in subtree
            # return sum, num
            if not curr:
                return (0, 0)

            leftval = dfs(curr.left)
            rightval = dfs(curr.right)

            localRet = (
                leftval[0] + rightval[0] + curr.val,
                leftval[1] + rightval[1] + 1,
            )

            avg = localRet[0] / localRet[1]
            if ret is None:
                ret = avg

            ret = max(ret, avg)

            return localRet

        dfs(root)

        return ret


# @lc code=end
