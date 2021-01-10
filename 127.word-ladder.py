#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import defaultdict
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        interDict = defaultdict(set)
        for word in wordList:
            ints = self.intermediates(word)
            for i in ints:
                interDict[i].update([word])

        queue = deque() 
        visited = set()

        queue.append((beginWord, 1))
        visited.add(beginWord)

        while queue:
            curr, level = queue.popleft()
            if curr == endWord:
                return level

            ints = self.intermediates(curr)
            for i in ints:
                neighbors = interDict[i]
                for neighbor in neighbors:
                    if not neighbor in visited:
                        queue.append((neighbor, level + 1))
                        visited.add(neighbor)
        
        return 0
    def intermediates(self, word: str):
        ret = []
        for idx in range(len(word)):
            ret.append(word[0:idx] + '*' + word[idx + 1:])
        return ret

# @lc code=end

