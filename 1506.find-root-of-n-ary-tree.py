#
# @lc app=leetcode id=1506 lang=python3
#
# [1506] Find Root of N-Ary Tree
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

from collections import defaultdict
class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        '''
        approach 1
        '''
        # treeSet = set(tree)
        # for node in tree:
        #     for child in node.children:
        #         treeSet.remove(child)
        
        # ret = None
        # for node in treeSet:
        #     ret = node
        #     break
        # return ret

        ret = 0
        for node in tree:
            ret += node.val
            for child in node.children:
                ret -= child.val
        
        for node in tree:
            if node.val == ret:
                return node
        
        return None




# @lc code=end

