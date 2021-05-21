#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        n = len(matrix)
        m = len(matrix[0])

        # rowSet = set()
        # colSet = set()

        if n == 1:
            if 0 in matrix[0]:
                for j in range(m):
                    matrix[0][j] = 0
                return
        
        if m == 1:
            for i in range(n):
                if matrix[i][0] == 0:
                    for i in range(n):
                        matrix[i][0] = 0
                    return

        zeroSet = set()
        oldZ = matrix[0][0]

        if not matrix[0][0]:
            zeroSet.add('col')
            zeroSet.add('row')
        
        matrix[0][0] = zeroSet


        for i in range(0,n):
            for j in range(0,m):
                if i == 0 and matrix[i][j] == 0:
                    matrix[0][0].add('row')
                elif j == 0 and matrix[i][j] == 0:
                    matrix[0][0].add('col')
                elif matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        print(matrix)
        zeroRow = [0 for _ in range(m)]

        for i in range(1, n):
            if matrix[i][0] == 0:
                matrix[i] = zeroRow

        for j in range(1, m):
            if matrix[0][j] == 0:
                for i in range(n):
                    matrix[i][j] = 0
        
        
        if 'row' in matrix[0][0]:
            for j in range(1, m):
                matrix[0][j] = 0
        
        if 'col' in matrix[0][0]:
            for i in range(1, n):
                matrix[i][0] = 0
        
        matrix[0][0] = 0 if len(matrix[0][0 > 0]) else oldZ

        '''
        O(1) extra space? but this fuckign sucks
        '''

        # def move(i, j, direc):
        #     if not (0 <= i < n) or not (0 <= j < m):
        #         return
            
        #     if matrix[i][j] != 0:
        #         matrix[i][j] = None

        #     if direc == 'n':
        #         move(i + 1, j, 'n')
        #     elif direc == 's':
        #         move(i - 1, j, 's')
        #     elif direc == 'e':
        #         move(i, j + 1, 'e')
        #     elif direc == 'w':
        #         move(i, j - 1, 'w')
        
        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][j] == 0:
        #             move(i, j, 'n')
        #             move(i, j, 's')
        #             move(i, j, 'e')
        #             move(i, j, 'w')
        
        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][j] is None:
        #             matrix[i][j] = 0




        
# @lc code=end

