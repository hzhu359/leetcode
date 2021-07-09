#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        from bisect import bisect_left
        from functools import reduce
        '''
        bisect_left will return the ~insertion~ point for the value in a certain sorted list
        because of this its range will be from
            0 (element is less than or equal to 0th index) to
            n (element is greater than last (n-1th) index)
        
        because of sorted property, we can search the first column to find the correct row in which to search.
        then we can just search the row (all with binary searc)

        the first column search will give us the insertion point of a number
        if that point is 0, we must check if the number is less than [0][0] (which means it doesn't exist)
            else it's equal to [0][0], so just return that

            i.e.:
            i = bisect_left(first_col)
            if arr[i][0] == target: return True
            if i == 0: return False

        otherwise the point will be in [1,n], so subtract 1 from that to get the row in which the target resides
            this is because the target will be less than or equal to the index it's on,
            so we look before it to get the containing row

            i.e.:
            i -= 1
        
        then we just binary search the proper row and check if its returned index matches with the target
        '''
        n = len(matrix)
        m = len(matrix[0])

        row = bisect_left([matrix[i][0] for i in range(n)], target)
        if row < n and matrix[row][0] == target:
            # checking for equals [0][0] or any first column element case
            return True
        row -= 1
        if row < 0:
            # checking for less than [0][0] case
            return False
        
        col = bisect_left(matrix[row],target)
        return True if col < m and matrix[row][col] == target else False


# @lc code=end

