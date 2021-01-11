/*
 * @lc app=leetcode id=973 lang=java
 *
 * [973] K Closest Points to Origin
 */

// @lc code=start
import java.util.*;
class Solution {
    public int[][] kClosest(int[][] points, int K) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((int[] x, int[] y) -> (euclidean(y) - euclidean(x)));

        for (int[] i : points) {
            pq.offer(i);
            if (pq.size() > K) {
                pq.poll();
            }
        }

        int[][] ret = new int[K][2];
        // int idx = 0;
        // for (int[] i : pq) {
        //     ret[idx++] = i;
        // }
        for (int i = 0; i < K; i++) {
            ret[i] = pq.poll();
        }

        return ret;
    }

    private static int euclidean(int[] x) {
        return x[0] * x[0] + x[1] * x[1];
    }
}
// @lc code=end

