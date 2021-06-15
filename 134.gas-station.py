#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # n = len(gas)
        # delta = []
        # total = 0
        # for i in range(n):
        #     delta.append(gas[i] - cost[i])
        #     total += delta[-1]
        
        # if total < 0:
        #     return -1
        
        # def runthrough(start):
        #     res = 0
        #     for i in range(n):
        #         res += delta[start]
        #         if res < 0:
        #             return False
        #         start = (start + 1) % n
        #     return True

        # for i in range(n):
        #     if runthrough(i):
        #         return i

        '''
        one runthrough pass

        i.e. we know that if we find some i...n path that ends up with >= 0 gas,
        we can get from i to 0.
        call this residual gas `after`

        the sum from 0...i can be called `before`.

        a solution exists if sum(delta) >= 0, so after + before >= 0

        say, for contradiction's sake, that `before` is a big negative number that's greater in magnitude than `after`
        (meaning that the travel from 0...i is more costly than gasly)

        then, `after` + `before` < 0, which contradicts the solution condition

        thus |`after`| >= |`before`| and if we start at i,
        we get to n with a residual of `after`,
        which we can use to get from 0 to i without dipping below 0.
        '''
        n = len(gas)
        gasTotal, startDex, currGas = 0,0,0
        delta = list(map(lambda gasi, costi: gasi - costi, gas, cost))

        for i in range(n):
            gasTotal += delta[i]
            currGas += delta[i]

            if currGas < 0:
                startDex = i + 1
                currGas = 0
        
        return startDex if gasTotal >= 0 else -1


# @lc code=end

