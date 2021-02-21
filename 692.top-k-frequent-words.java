import java.util.HashMap;

/*
 * @lc app=leetcode id=692 lang=java
 *
 * [692] Top K Frequent Words
 */

// @lc code=start
import java.util.*;
class Solution {
    public List<String> topKFrequent(String[] words, int k) {

        HashMap<String, Integer> hmap = new HashMap<>();

        for (String word : words) {
            hmap.put(word, hmap.getOrDefault(word, 0) + 1);
        }
        Set<Map.Entry<String, Integer>> hmapEntries = hmap.entrySet();
        PriorityQueue<Map.Entry<String, Integer>> pq = new PriorityQueue<>((x, y) -> x.getValue() - y.getValue());

        for (Map.Entry<String, Integer> entry : hmapEntries) {
            pq.add(entry);
            if (pq.size() > k) {
                pq.poll();
            }
        }

        ArrayList<String> ret = new ArrayList<>();

        while (!pq.isEmpty()) {
            int occs = pq.peek().getValue();
            ArrayList<String> level = new ArrayList<>();
            while (!pq.isEmpty() && pq.peek().getValue() == occs) {
                level.add(pq.poll().getKey());
            }
            level.sort(null);
            for (int i = level.size() - 1; i >= 0; i--) {
                ret.add(level.get(i));
            }
        }
        Collections.reverse(ret);
        return ret;
    }
}
// @lc code=end

