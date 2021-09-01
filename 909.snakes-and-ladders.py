#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#

# @lc code=start
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        from collections import deque

        n = len(board)
        queue = deque()
        visited = [False for _ in range(n**2)]
        level = 0


        def boardVal(i):
            rprime = (i - 1) // n
            r = (n - 1) - rprime

            cprime = (i - 1) % n
            c = n - 1 - cprime if rprime % 2 else cprime

            return board[r][c]
        
        def populateQueue(i):
            for j in range(i + 1, min(i + 6, n ** 2) + 1):
                bv = boardVal(j)

                if j == n ** 2 or bv == n ** 2:
                    return True

                if not visited[bv]:
                    if bv == -1:
                        queue.append(j)
                    else:
                        queue.append(bv)
                
            return False
            
        if boardVal(1) != -1 or boardVal(n ** 2) != -1:
            return -1
        
        # queue has 1-n^2 vals
        queue.append(1)


        while queue:
                for i in range(len(queue)):
                    curr = queue.popleft()
                    if not visited[curr]:
                        visited[curr] = True

                        if populateQueue(curr):
                            return level + 1
                        
                level += 1
            
        return -1





        




# @lc code=end

