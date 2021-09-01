#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#

# @lc code=start
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        edgeSet = set()
        letterSet = set()
        maxLen = 0

        for word in words:
            maxLen = max(maxLen, len(word))
            letterSet.update(list(word))

        # groups roots together
        def kIterate(k):
            if not k < maxLen:
                return
            cont = 0
            ret = []
            rootGroup = ''
            for idx, word in enumerate(words):
                if len(word) <= k:
                    if word[:k] == rootGroup and len(ret) >= 1:
                        return True
                    continue
                if word[:k] == rootGroup:
                    # keep adding to ret
                    ret.append(word[k])
                else:
                    # start new group
                    if len(ret) > 1:
                        groupIterate(ret)
                        cont += 1
                    rootGroup = word[:k]
                    ret = [word[k]]
            
            if len(ret) > 1:
                groupIterate(ret)
                cont += 1
            
            if cont:
                if kIterate(k + 1):
                    return True

        
        # after the root is chopped off, this evaluates the remaining diffs
        def groupIterate(groupLetters):
            ret = []
            letterGroup = ''
            for letter in groupLetters:
                if letter != letterGroup:
                    ret.append(letter)
                    letterGroup = letter 

                if len(ret) == 2:
                    edgeSet.add(tuple(ret))
                    ret = [letterGroup]
        
        from collections import defaultdict
        graph = defaultdict(list)

        def constructGraph():
            for edge in edgeSet:
                graph[edge[0]].append(edge[1])
        
        retstr = ''
        visitedSet = set()
        recSet = set()

        def dfs(curr):
            nonlocal retstr
            ret = False
            if curr in visitedSet:
                return
            
            visitedSet.add(curr)
            recSet.add(curr)
            
            for v in graph[curr]:
                if not v in visitedSet:
                    if dfs(v):
                        ret = True
                
                if v in recSet:
                    ret = True

            retstr += curr
            recSet.remove(curr)
            return ret



        if kIterate(0):
            return ''
        constructGraph()
        for letter in letterSet:
            if dfs(letter):
                return ''
        return retstr[::-1]



# @lc code=end

