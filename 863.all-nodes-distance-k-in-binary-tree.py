#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        '''
        two methods:

        1. searchDown
            starts at a node and dfs downwards until we hit a level
            a parameter called distance is passed in here and denotes the distance away from the node
            i.e. going downwards will increase this distance

        2. searchUp
            starts at a node and dfs for the target node by searchUp on left and right children
            once we're on the target node, we searchDown from there
            and return 0

            on subsequent searchUp calls (up the tree),
            we'll return the successful return value + 1 and searchDown using the distance returned
                ONLY searchDown on the branch that wasn't already explored by searchUp
                i.e. if the searchUp call from the right child returns a number,
                don't  call searchDown on that side because searchUp already explored that side:
            
            if rreturn:
                if rreturn == targetDist:
                    ret.add(curr)
                res = searchDown(curr.left, rreturn)
                return res + 1
            elif lreturn:
                if lreturn == targetDist:
                    ret.add(curr)
                res = searchDown(curr.right, lreturn)
                return res + 1
            else:
                return None
        '''
        ret = []

        def searchDown(curr, dist):
            if not curr:
                return
            if dist == k:
                ret.append(curr.val)
            elif dist < k:
                searchDown(curr.left, dist + 1)
                searchDown(curr.right, dist + 1)
        
        def searchUp(curr):
            if not curr:
                return None
            if curr == target:
                searchDown(curr, 0)
                return 1

            rightres = searchUp(curr.right)
            if not rightres is None:
                if rightres == k:
                    ret.append(curr.val)
                    return None
                searchDown(curr.left, rightres + 1)
                return rightres + 1
            leftres = searchUp(curr.left)
            if not leftres is None:
                if leftres == k:
                    ret.append(curr.val)
                    return None
                searchDown(curr.right, leftres + 1)
                return leftres + 1
            else:
                return None
        
        searchUp(root)
        return ret




# @lc code=end

