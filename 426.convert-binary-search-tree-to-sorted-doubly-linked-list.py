#
# @lc app=leetcode id=426 lang=python3
#
# [426] Convert Binary Search Tree to Sorted Doubly Linked List
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        ret = None
        last = None

        def dfs(curr):
            nonlocal ret
            if curr is None:
                return (None, None)
            
            leftret = dfs(curr.left)

            if leftret is (None, None) and ret is None:
                ret = curr
            
            elif not leftret is (None, None):
                leftret[1].right = curr
                curr.left = leftret[1]
            
            rightret = dfs(curr.right)

            if not rightret is (None, None):
                curr.right = rightret[0]
                rightret[0].left = curr
            
            # returns should return max/min of each branch
            minElems = [leftret[0], rightret[0], curr]
            minElems = list(filter(lambda x: x is not None, minElems))
            minn = min(minElems, key=lambda x: x.val)

            maxElems = [leftret[1], rightret[1], curr]
            maxElems = list(filter(lambda x: x is not None, maxElems))
            maxx = max(maxElems, key=lambda x: x.val)

            return (minn, maxx)
        
        minn, maxx = dfs(root)
        if minn and maxx:
            maxx.right = minn
            minn.left = maxx
        return ret
            


            




# @lc code=end

