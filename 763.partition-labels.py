#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, S: str) -> list[int]:

        firstLast = {}

        for idx, char in enumerate(S):
            if not char in firstLast:
                # first occ
                firstLast[char] = [idx, idx]
            else:
                # last occ
                firstLast[char][1] = idx

        firstLastList = list(firstLast.values())
        firstLastList.sort(key=lambda x: x[0])
        print(firstLast)
        print(firstLastList)

        ret = []
        currIntvl = firstLastList[0]
        for intvl in firstLastList:
            if currIntvl[0] <= intvl[0] <= currIntvl[1]:
                print('union')
                print(currIntvl)
                print(intvl)
                # union interval
                currIntvl[0], currIntvl[1] \
                    = min(currIntvl[0], intvl[0]), max(currIntvl[1], intvl[1])
            else:
                ret.append(currIntvl[1] - currIntvl[0] + 1)
                currIntvl = intvl
                print('add')
                print(currIntvl)

        if currIntvl:
            ret.append(currIntvl[1] - currIntvl[0] + 1)
        return ret




    
# @lc code=end

