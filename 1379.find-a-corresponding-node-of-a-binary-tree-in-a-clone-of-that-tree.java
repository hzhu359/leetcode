/*
 * @lc app=leetcode id=1379 lang=java
 *
 * [1379] Find a Corresponding Node of a Binary Tree in a Clone of That Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.util.*;


class Solution {
    /**
     * solution
     * we'll just do a BFS on the tree with the original tree while trying to match the reference w/ target
     * if we count the number of iterations, we can do the same number of BFS iterations in the cloned
     *      tree to end up with the same node
     * this is agnostic of repetition because it'll compare and execute using the same process
     */
    // public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target) {
    //     int iterations = 0;
    //     Queue<TreeNode> q = new LinkedList<>();
    //     q.offer(original);

    //     while (!q.isEmpty()) {
    //         TreeNode curr = q.poll();
    //         if (curr == target) {
    //             break;
    //         }
    //         iterations += 1;
    //         if (curr.left != null) {
    //             q.offer(curr.left);
    //         }

    //         if (curr.right != null) {
    //             q.offer(curr.right);
    //         }
    //     }

    //     q.clear();
    //     q.offer(cloned);

    //     int clonedIterations = 0;
    //     while (!q.isEmpty()) {
    //         TreeNode curr = q.poll();
    //         if (clonedIterations == iterations) {
    //             return curr;
    //         }
    //         clonedIterations += 1;
    //         if (curr.left != null) {
    //             q.offer(curr.left);
    //         }

    //         if (curr.right != null) {
    //             q.offer(curr.right);
    //         }
    //     }
    //     return null;
    // }
    
    /**
     * non-repeat-agnostic version
     */
    public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target) {
        return dfs(cloned, target.val);
        // Queue<TreeNode> q = new LinkedList<>();
        // q.offer(cloned);

        // while (!q.isEmpty()) {
        //     TreeNode curr = q.poll();
        //     if (curr.val == target.val) {
        //         return curr;
        //     }
        //     if (curr.left != null) {
        //         q.offer(curr.left);
        //     }

        //     if (curr.right != null) {
        //         q.offer(curr.right);
        //     }
        // }

        // return null;
    }

    TreeNode dfs(TreeNode curr, int target) {
        if (curr == null) {
            return null;
        }
        if (curr.val == target) {
            return curr;
        } 
        TreeNode l = dfs(curr.left, target);
        TreeNode r = dfs(curr.right, target);

        return (l != null)? l : r;
    }

}
// @lc code=end

