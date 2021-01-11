#
# @lc app=leetcode id=1649 lang=python3
#
# [1649] Create Sorted Array through Instructions
#

# @lc code=start
import bisect
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        '''
        bisect
        '''
        ret = 0
        running = []
        for x in instructions:
            low = bisect.bisect_left(running, x)
            high = bisect.bisect_right(running, x)
            ret += min(low, len(running) - high)
            bisect.insort(running, x)
        MOD = 10**9 + 7
        return ret % MOD

        '''
        mergesort
        '''
        # def mergeSort(arr, mergeFunc):
        #     if len(arr) <= 1:
        #         return

        #     mid = len(arr) // 2
        #     left = arr[:mid]
        #     right = arr[mid:]

        #     mergeSort(left, mergeFunc)
        #     mergeSort(right, mergeFunc)
        #     mergeFunc(left, right, arr)

        # def smMerge(left, right, arr):
        #     '''
        #     sorts in ascending order
        #     records l->r jumps
        #     '''
        #     i = 0
        #     j = 0
        #     idx = 0

        #     while i < len(left) and j < len(right):
        #         # no jump case
        #         if left[i][0] <= right[j][0]:
        #             arr[idx] = left[i]
        #             idx += 1
        #             i += 1

        #         # jump case
        #         else:
        #             arr[idx] = right[j]
        #             smaller[right[j][1]] += len(left) - i
        #             idx += 1
        #             j += 1
            
        #     while i < len(left):
        #         arr[idx] = left[i]
        #         idx += 1
        #         i += 1

        #     while j < len(right):
        #         arr[idx] = right[j]
        #         idx += 1
        #         j += 1

        # def lgMerge(left, right, arr):
        #     '''
        #     sorts in descending order
        #     records l->r jumps
        #     '''
        #     i = 0
        #     j = 0
        #     idx = 0

        #     while i < len(left) and j < len(right):
        #         # no jump case
        #         if left[i][0] >= right[j][0]:
        #             arr[idx] = left[i]
        #             idx += 1
        #             i += 1

        #         # jump case
        #         else:
        #             arr[idx] = right[j]
        #             larger[right[j][1]] += len(left) - i
        #             idx += 1
        #             j += 1
            
        #     while i < len(left):
        #         arr[idx] = left[i]
        #         idx += 1
        #         i += 1

        #     while j < len(right):
        #         arr[idx] = right[j]
        #         idx += 1
        #         j += 1

        # n = len(instructions)
        # smaller = [0] * n
        # larger = [0] * n
        # MOD = 10 ** 9 + 7

        # smArr = [(entry, idx) for idx, entry in enumerate(instructions)]
        # lgArr = smArr[:]

        # mergeSort(smArr, smMerge)
        # mergeSort(lgArr, lgMerge)

        # ret = 0
        # for entry in zip(smaller, larger):
        #     ret += min(entry)
        # return ret % MOD

# @lc code=end

