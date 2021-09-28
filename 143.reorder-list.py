#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # silly array version

        # lst = []

        # curr = head

        # while curr:
        #     lst.append(curr)
        #     curr = curr.next

        # n = len(lst)

        # i = 0
        # mods = []
        # while i < n :
        #     curr = None
        #     if not i % 2:
        #         #beg
        #         curr = i // 2
        #     else:
        #         curr = n - i // 2 - 1
        #     mods.append(curr)
        #     i += 1

        # for i in range(n - 1):
        #     curr = mods[i]
        #     next = mods[i + 1]
        #     lst[curr].next = lst[next]

        # lst[mods[-1]].next = None

        # return lst[0]

        def addNext(curr, next):
            n = curr.next
            curr.next = next
            next.next = n

        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        # have valid head

        i = 0
        curr = head
        beforeSecond = None

        while i < (n + 1) // 2:
            if i == (n + 1) // 2 - 1:
                beforeSecond = curr
            curr = curr.next
            i += 1

        # curr is at second half
        headptr = head

        def reverse(innercurr):
            nonlocal headptr

            if innercurr == None:
                return

            reverse(innercurr.next)
            outercurrnext = headptr.next
            addNext(headptr, innercurr)
            headptr = outercurrnext

        reverse(curr)
        if not n % 2:
            # even case
            curr.next = None
        else:
            beforeSecond.next = None

        return head


# @lc code=end
