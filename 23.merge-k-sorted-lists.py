#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq

        # sketch: add all list nodes to a heap and each time you pop, push on the next

        ret = ListNode()
        retTail = ret

        heap = []
        idx = 0
        for curr in lists:
            if curr:
                heap.append((curr.val, idx, curr))
                idx += 1
        
        heapq.heapify(heap)

        while heap:
            curr = heapq.heappop(heap)[2]
            currNext = curr.next

            retTail.next = curr
            retTail = retTail.next
            curr.next = None

            if currNext:
                heapq.heappush(heap, (currNext.val, idx, currNext))
                idx += 1
        
        return ret.next


        '''

        retHead = ListNode()
        retCurr = retHead

        # for heapq to differentiate values
        insertTime = 0

        h = []
        heapq.heapify(h)

        def insertIntoRet(listNode):
            nonlocal retCurr
            # put into ret list
            retCurr.next = listNode
            retCurr = listNode

            # increment and requeue listNode
            listNode = listNode.next
            queue(listNode)
            
            # # sever retNode
            # retCurr.next = None
        
        def queue(listNode):
            nonlocal insertTime
            if not listNode is None:
                heapq.heappush(h, (listNode.val, insertTime, listNode))
                insertTime += 1
        
        for listNode in lists:
            queue(listNode)
        
        while h:
            curr = heapq.heappop(h)
            insertIntoRet(curr[-1])
        
        return retHead.next
        '''




        
# @lc code=end

