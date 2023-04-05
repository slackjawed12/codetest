/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> preorderTraversal(List<Integer> cur, TreeNode root) {
        if(root==null) return cur;
        else {
            cur.add(root.val);
            cur = preorderTraversal(cur, root.left);
            cur = preorderTraversal(cur, root.right);
            return cur;
        }
    }
    public List<Integer> preorderTraversal(TreeNode root) {
        return preorderTraversal(new ArrayList(), root);
    }
}