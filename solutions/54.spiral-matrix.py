#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # m = len(matrix)
        # n = len(matrix[0])
        # ret = []
        # if m == 1:
        #     # completely horizontal
        #     for x in matrix[0]:
        #         ret.append(x)
        #     return ret
        # if n == 1:
        #     # completely vertical
        #     for x in matrix:
        #         ret.append(x[0])
        #     return ret
        
        # i = 0
        # j = 0

        # icount = m
        # jcount = n
        # step = 1

        # while icount != 0 and jcount != 0:
        #     for _ in range(jcount):
        #         ret.append(matrix[i][j])
        #         j += step
        #     j -= step
        #     i += step
        #     jcount -= 1 

        #     icount -= 1
        #     for _ in range(icount):
        #         ret.append(matrix[i][j])
        #         i += step
        #     i -= step
        #     step *= -1

        #     j += step
        # return ret

        ret = []

        def recurse(arr: list, flip: bool):
            '''
            in our spiral matrix, we're pretty much just shaving off the top and sides

            if not flip:
                shave off top and right side
            else:
                shave off bottom and left side

            after that we can pass our shaved array to the next recursion and continue on

            base case is when we have an n x 1 or 1 x m array
            '''
            n = len(arr)
            m = len(arr[0])

            if n == 1:
                # horiz case
                for x in arr[0] if not flip else reversed(arr[0]):
                    ret.append(x)
                return
            if m == 1:
                # vert case
                for x in arr if not flip else reversed(arr):
                    ret.append(x[0])
                return

            top = None
            side = None
            if not flip:
                # top and right
                top = arr.pop(0)
                side = []
                for x in arr:
                    side.append(x.pop())
            else:
                # bot and left
                top = reversed(arr.pop())
                side = []
                for x in arr:
                    side.append(x.pop(0))
                side = reversed(side)
            
            for x in top:
                ret.append(x)
            for x in side:
                ret.append(x)

            recurse(arr, not flip)
            

        recurse(matrix, False)
        return ret



# @lc code=end

