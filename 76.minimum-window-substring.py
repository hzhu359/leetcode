#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        n = len(s)
        ogCounter = Counter(t)
        hmap = dict()

        i = 0
        j = i

        uniques = 0

        ret = None

        while j < n:
            # expand until good
            while j < n and uniques < len(ogCounter.keys()):
                curr = s[j]
                j += 1

                if curr in ogCounter.keys():
                    hmap[curr] = hmap.get(curr, 0) + 1

                    if hmap[curr] == ogCounter[curr]:
                        uniques += 1

                    # print(s[i:j])
                    if uniques == len(ogCounter.keys()):
                        # print(s[i:j], "good")
                        if ret is None or len(s[i:j]) < len(ret):
                            ret = s[i:j]

            # contract until bad
            while (i < j) and uniques >= len(ogCounter.keys()):
                curr = s[i]
                i += 1

                if curr in ogCounter.keys():
                    hmap[curr] -= 1

                    if hmap[curr] < ogCounter[curr]:
                        uniques -= 1

                if uniques == len(ogCounter.keys()):
                    # print(s[i:j], "good")
                    if ret is None or len(s[i:j]) < len(ret):
                        ret = s[i:j]
                else:
                    break

            # print(s[i:j])
            # print("bad")

        return ret if ret else ""


# @lc code=end
