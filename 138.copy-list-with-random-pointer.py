#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        oldPtrMap = {}
        newPtrArr = []

        index = 0
        ret = Node(head.val)

        curr = head
        retCurr = ret

        while curr.next:
            retCurr.next = Node(curr.next.val)

            oldPtrMap[curr] = index
            newPtrArr.append(retCurr)
            index += 1

            curr = curr.next
            retCurr = retCurr.next
        
        oldPtrMap[curr] = index
        newPtrArr.append(retCurr)
        index += 1
        oldPtrMap[None] = index
        newPtrArr.append(None)

        curr = head
        retCurr = ret

        while retCurr:
            retCurr.random = newPtrArr[oldPtrMap[curr.random]]
            curr = curr.next
            retCurr = retCurr.next
        
        return ret
        



# @lc code=end

