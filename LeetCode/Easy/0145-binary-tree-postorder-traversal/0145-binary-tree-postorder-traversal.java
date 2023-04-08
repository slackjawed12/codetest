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
    public List<Integer> postorderTraversal(List<Integer> cur, TreeNode root) {
        if(root==null) {
            return cur;
        } else {
            cur = postorderTraversal(cur, root.left);
            cur = postorderTraversal(cur, root.right);
            cur.add(root.val);
            return cur;
        }
    }
    
    
    public List<Integer> postorderTraversal(TreeNode root) {
        return postorderTraversal(new ArrayList<Integer>(), root);
    }
}