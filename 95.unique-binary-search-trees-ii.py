#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = dict()

        def generateSubtrees(start, end):
            # generates subtrees by picking a root in [start, end]
            # and recursively generating smaller subtrees in [start, i - 1], [i + 1, end], ...
            # inclusive end
            if (start, end) in dp:
                return dp[(start, end)]

            ret = []

            if start > end:
                # need this so we can iterate leftTrees and rightTrees even on empty return
                return [None]

            for i in range(start, end + 1):
                leftTrees = generateSubtrees(start, i - 1)
                rightTrees = generateSubtrees(i + 1, end)
                for lt in leftTrees:
                    for rt in rightTrees:
                        curr = TreeNode(i)
                        curr.left = lt
                        curr.right = rt
                        ret.append(curr)
            
            dp[(start, end)] = ret
            return ret

        return generateSubtrees(1, n)


# @lc code=end
