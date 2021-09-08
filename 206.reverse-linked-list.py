#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        ret = None

        def reverse(curr):
            nonlocal ret
            # returns reversed list from this point onwards
            if not curr:
                return None

            restOfList = reverse(curr.next)

            if not restOfList:
                ret = curr
            else:
                restOfList.next = curr

            return curr

        result = reverse(head)
        if result:
            result.next = None

        return ret


# @lc code=end
