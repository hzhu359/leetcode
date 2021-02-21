/*
 * @lc app=leetcode id=2 lang=java
 *
 * [2] Add Two Numbers
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode ret = new ListNode(-1);
        ListNode retCurr = ret;

        while (!(l1 == null && l2 == null)) {
            int l1val = l1 == null? 0 : l1.val;
            int l2val = l2 == null? 0 : l2.val;
            int sum = l1val + l2val + carry;
            int toAddVal = sum % 10; // gives us least significant digit of sum
            carry = sum / 10; // gives us carry out into next iteration
            retCurr.next = new ListNode(toAddVal);
            retCurr = retCurr.next;
            if (l1 != null) {
                l1 = l1.next;
            }
            if (l2 != null) {
                l2 = l2.next;
            }
        }
        // at this point, both l1 and l2 are null, so we've looked at all nodes in l1 and l2
        // so we either have a carry in or we can just return
        if (carry > 0) {
            retCurr.next = new ListNode(1);
            retCurr = retCurr.next;
        }
        return ret.next;
    }
}
// @lc code=end

