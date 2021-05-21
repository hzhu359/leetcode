#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        from collections import deque
        # def rec(curr, index):
        #     if not curr:
        #         return
        #     if (index < left) or (index > right):
        #         self.dCurr.next = ListNode(val = curr.val)
        #         self.dCurr = self.dCurr.next
        #         rec(curr.next, index + 1)
        #     elif (index >= left) and (index < right):
        #         rec(curr.next, index + 1)
        #         self.dCurr.next = ListNode(curr.val)
        #         self.dCurr = self.dCurr.next
        #     elif (index == right):
        #         self.ext = curr.next
        #         self.dCurr.next = ListNode(curr.val)
        #         self.dCurr = self.dCurr.next
        #     else:
        #         print('uh oh!')
        # inplace recursion


        def rec(curr, index, q:deque):
            if not curr:
                return
            if (index < left) or (index > right):
                rec(curr.next, index + 1, q)
            elif (index >= left) and (index < right):
                q.append(curr.val)
                rec(curr.next, index + 1, q)
                curr.val = q.popleft()
            elif (index == right):
                q.append(curr.val)
                curr.val = q.popleft()
            else:
                print('uh oh!')

        q = deque()
        rec(head, 1, q)
        return head



# @lc code=end