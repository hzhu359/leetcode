#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get to the one before and connect to next.next

        def recurse(curr):
            if curr is None:
                return 1, None
            currN, nextNode = recurse(curr.next)
            curr.next = nextNode
            return currN + 1, curr.next if currN == n else curr

        return recurse(head)[1]

        # nodes = []
        # curr = head
        # while curr:
        #     nodes.append(curr)
        #     curr = curr.next

        # length = len(nodes)

        # if length == 1:
        #     return None

        # dex = length - n

        # if dex == 0:
        #     return nodes[dex + 1]
        # else:
        #     nodes[dex - 1].next = nodes[dex].next
        #     return head


# @lc code=end
