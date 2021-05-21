#
# @lc app=leetcode id=1658 lang=python3
#
# [1658] Minimum Operations to Reduce X to Zero
#

# @lc code=start
def main():
    s = Solution()
    nums = [8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309] 
    x = 134365
    print(s.minOperations(nums, x))
from collections import deque
class Solution:
    def minOperations(self, nums, x) -> int:
        nums = deque(nums)
        ret = 0

        while x > 0 and nums:
            left = nums[0]
            right = nums[-1]
            ret += 1

            if left == x:
                x -= nums.popleft()
            elif right == x:
                x -= nums.pop()
            elif left < x < right:
                x -= nums.popleft()
            elif right < x < left:
                x -= nums.pop()
            else:
                if right > left:
                    x -= nums.pop()
                else:
                    x -= nums.popleft()

        print(nums)
        print(x)
        print(ret)
        return -1 if (x < 0 or (not nums and x > 0)) else ret

if __name__ == "__main__":
    main()
# @lc code=end

