#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # naive approach: do a matching for every subRoot match in OG tree
        def match(ogcurr, subcurr):
            if not ogcurr or not subcurr:
                # if one is None, other should be None
                return (ogcurr is None) and (subcurr is None)
                
            if not ogcurr.val == subcurr.val:
                return False
            
            return match(ogcurr.left, subcurr.left) and match(ogcurr.right, subcurr.right)
        
        def dfs(curr):
            if not curr:
                return False
            
            if curr.val == subRoot.val and match(curr, subRoot):
                return True
            
            return dfs(curr.left) or dfs(curr.right)
        
        return dfs(root)


# @lc code=end

