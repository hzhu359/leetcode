#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        ret = []

        def dfs(curr, path, sum_of_path):
            if not curr:
                return
            elif not curr.left and not curr.right and (sum_of_path + curr.val) == targetSum:
                ret.append(path + [curr.val])
            else:
                dfs(curr.left, path + [curr.val], sum_of_path + curr.val)
                dfs(curr.right, path + [curr.val], sum_of_path + curr.val)

        
        dfs(root, [], 0)

        return ret


        
# @lc code=end

