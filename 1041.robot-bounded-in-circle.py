#
# @lc app=leetcode id=1041 lang=python3
#
# [1041] Robot Bounded In Circle
#

# @lc code=start
class Solution:
    # def isRobotBounded(self, instructions: str) -> bool:
    #     '''
    #     STOOPID VERSION

    #     i believe periodicity in this case is bounded by 4 iterations?
    #     so if at any point we're at (0,0) in 4 iterations just return true
    #     '''

    #     # N = 0, E = 1, S = 2, W = 3
    #     finalDir = 0
    #     finalx, finaly = 0, 0
    #     dirDict = {
    #         0: (0, 1),
    #         1: (1, 0),
    #         2: (0, -1),
    #         3: (-1, 0)
    #     }

    #     for _ in range(4):
    #         for c in instructions:
    #             if c == 'R':
    #                 finalDir = (finalDir + 1) % 4
    #             elif c == 'L':
    #                 finalDir = (finalDir - 1) % 4
    #             else:
    #                 dd = dirDict[finalDir]
    #                 finalx += dd[0]
    #                 finaly += dd[1]
    #         if not finalx and not finaly:
    #             return True
    #     return False


    def isRobotBounded(self, instructions: str) -> bool:
        '''
        if after x iterations of instructions we return to origin,
            then our motion is periodic
        this is because even if we're pointing in different directions,
            if we start at the origin at the beginning of an iteration,
            it's just the start, but with a rotated plane

        i think you just need to be pointing in any different direction
            in order to be peeriodic 
        '''
        # N = 0, E = 1, S = 2, W = 3
        finalDir = 0
        finalx, finaly = 0, 0
        dirDict = {
            0: [0, 1],
            1: [1, 0],
            2: [0, -1],
            3: [-1, 0]
        }

        for char in instructions:
            if char == 'R':
                finalDir = (finalDir + 1) % 4
            elif char == 'L':
                finalDir = (finalDir - 1) % 4
            else:
                dd = dirDict[finalDir]
                finalx += dd[0]
                finaly += dd[1]
        
        if not finalx and not finaly:
            return True
        
        if finalDir:
            return True
        
        return False

        # LMAOOOOOOOOOOOOO


# @lc code=end

