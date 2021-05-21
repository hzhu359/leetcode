#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.backingSet = set()

        self.backingList = []
        self.indexTable = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        # if val in self.backingSet:
        #     return False
        # else:
        #     self.backingSet.add(val)
        #     return True
        if val in self.indexTable:
            return False
        else:
            self.backingList.append(val)
            self.indexTable[val] = len(self.backingList) - 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # try:
        #     self.backingSet.remove(val)
        #     return True
        # except KeyError as e:
        #     return False
        if not val in self.indexTable:
            return False
        else:
            temp, idx = self.backingList[-1], self.indexTable[val]
            self.backingList[idx] = temp
            self.indexTable[temp] = idx

            self.backingList.pop()
            del self.indexTable[val]
            return True


    def getRandom(self) -> int:
        from random import randint
        """
        Get a random element from the set.
        """
        # from random import randint
        # n = len(self.backingSet)
        # rand = randint(0, n-1)

        # for idx, entry in enumerate(self.backingSet):
        #     if idx == rand:
        #         return entry
        #         break
        return self.backingList[randint(0, len(self.backingList) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

