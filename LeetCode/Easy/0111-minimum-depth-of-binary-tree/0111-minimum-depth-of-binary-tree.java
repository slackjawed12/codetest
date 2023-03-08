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
    public int minDepth(TreeNode root, int inter){
        if(root.left==null && root.right==null) { // leaf node
            return inter;
        } else if (root.left==null && root.right!= null) {
            return minDepth(root.right, inter+1);
        } else if (root.left!=null && root.right== null){
            return minDepth(root.left, inter+1);
        } else {
            return Math.min(minDepth(root.left, inter+1), minDepth(root.right, inter+1));
        }
    }
    public int minDepth(TreeNode root) {
        if(root==null) return 0;
        else {
            return minDepth(root, 1);
        }
    }
}