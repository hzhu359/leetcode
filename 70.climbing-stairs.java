ub*
 * @lc app=leetcode id=70 lang=java
 *
 * [70] Climbing Stairs
 */

// @lc code=start
class Solution {
    public int climbStairs(int n) {
        // dp[0] = 1;
        // for (int i = 0; i < dp.length - 1; i++) {
        //     if ((i + 1) < dp.length) {
        //         dp[i + 1] += dp[i];
        //     }
        //     if ((i + 2) < dp.length) {
        //         dp[i + 2] += dp[i];
        //     }
        // }

        // return dp[dp.length - 1];
        int start = 1;
        int oneIncr = 0;
        int twoIncr = 0;
        for (int i = 0; i < n; i++) {
            oneIncr += start;
            twoIncr += start;

            start = oneIncr;
            oneIncr = twoIncr;
            twoIncr = 0;
        }
        return start;
    }
}
// @lc code=end

